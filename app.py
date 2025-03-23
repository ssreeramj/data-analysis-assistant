from typing import Optional, Tuple

import gradio as gr
import pandas as pd
from PIL import Image

from agent.implementation import stream_graph_updates


def process_dataset(file) -> Optional[pd.DataFrame]:
    """Load dataset from uploaded file"""
    try:
        if file.name.endswith(".csv"):
            return pd.read_csv(file.name)
        elif file.name.endswith((".xlsx", ".xls")):
            return pd.read_excel(file.name)
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def query_data(dataset: pd.DataFrame, question: str) -> Tuple[str, Image.Image]:
    """
    Call agent to process the question and generate visualization
    """
    # Set the global df in the implementation module
    import agent.implementation

    agent.implementation.df = dataset

    # Get response from agent
    response = stream_graph_updates(question)

    # Check if visualization was generated
    try:
        visualization = Image.open("figure.png")
    except:
        visualization = None

    if "final_answer" in response:
        return response["final_answer"].final_answer, visualization
    return "Failed to generate response", None


def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Data Analysis Assistant")

        with gr.Row():
            with gr.Column():
                file_input = gr.File(label="Upload your CSV or Excel file")
                dataset_status = gr.Textbox(label="Dataset Status", interactive=False)

        # Add Examples component after the file input
        gr.Examples(
            examples=["data/sales-data-sample.csv"],
            inputs=file_input,
            label="Example Datasets",
        )

        # Add DataFrame preview component
        dataset_preview = gr.Dataframe(label="Dataset Preview", interactive=False)

        question_input = gr.Textbox(
            label="Ask a question about your data",
            placeholder="e.g., What is the average age in the dataset?",
            interactive=False,
        )

        with gr.Row():
            text_output = gr.Textbox(label="Response")
            plot_output = gr.Image(label="Visualization")

        # Store dataset in state
        dataset_state = gr.State()

        def handle_file_upload(file):
            if file is None:
                return "No file uploaded", None, gr.update(interactive=False), None

            df = process_dataset(file)
            if df is not None:
                # Return preview of first few rows
                return (
                    "Dataset loaded successfully!",
                    df,
                    gr.update(interactive=True),
                    df.head(),
                )
            return "Error loading dataset", None, gr.update(interactive=False), None

        def handle_question(question, df):
            if df is None:
                return "Please upload a dataset first", None
            response, visualization = query_data(df, question)
            return response, visualization

        file_input.change(
            handle_file_upload,
            inputs=[file_input],
            outputs=[dataset_status, dataset_state, question_input, dataset_preview],
        )

        question_input.submit(
            handle_question,
            inputs=[question_input, dataset_state],
            outputs=[text_output, plot_output],
        )

    demo.launch()


if __name__ == "__main__":
    main()
