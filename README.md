# Data Analysis Assistant with LLM

![Data Analysis Assistant Demo](assets/demo.gif)

A powerful data analysis application that combines the capabilities of Large Language Models (LLM) with interactive data visualization. Users can upload their datasets and ask questions in natural language to get insights and visualizations.

## Features

- 📊 Support for CSV and Excel file formats
- 💬 Natural language queries about your data
- 📈 Automatic visualization generation
- 🔍 Interactive data preview
- 📝 Detailed textual explanations
- 🎯 Example datasets included

## Technical Stack

- **Frontend**: Gradio (Python web framework for ML applications)
- **Backend**: 
  - LangGraph for LLM orchestration
  - OpenAI GPT-4 for natural language understanding
  - Pandas for data manipulation
  - Matplotlib for visualization generation
- **Agent Architecture**: Custom implementation using LangGraph for structured conversation flow

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ssreeramj/data-analysis-assistant.git
cd data-analysis-assistant
```

2. Create a virtual environment and activate it:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required packages:
```bash
uv pip install -r uv.lock
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following:
```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
gradio app.py
```

2. Open your web browser and navigate to `http://localhost:7860`

3. Upload your dataset or use one of the provided examples

4. Ask questions about your data in natural language, for example:
   - "What is the distribution of sales across different products?"
   - "Show me the trend of revenue over time"
   - "Which department has the highest average salary?"

## Project Structure

data-analysis-assistant/  
├── app.py # Main Gradio application  
├── agent/  
│ ├── implementation.py # LLM agent implementation  
│ └── stub.py # Agent interface definitions  
├── data/ # Example datasets  
│ └── sales-data-sample.csv  
├── assets/ # Images and demo files  
│ └── demo.gif  
└── requirements.txt # Project dependencies  

## How It Works

1. **Data Loading**: The application accepts CSV or Excel files and loads them into a pandas DataFrame.

2. **Query Processing**: When a user asks a question, it's processed by a custom LangChain agent that:
   - Analyzes the question intent
   - Generates appropriate pandas code
   - Creates relevant visualizations
   - Provides natural language explanations

3. **Visualization**: The system automatically selects the most appropriate visualization type based on:
   - The nature of the question
   - The data structure
   - The type of analysis required

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with [Gradio](https://gradio.app/)
- Powered by [LangGraph](https://www.langchain.com/langgraph)
- Boilerplate Langgraph Code [LangGraph Code](https://build.langchain.com/)
- Visualization using [Matplotlib](https://matplotlib.org/)

## Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/ssreeramj/data-analysis-assistant/issues) page
2. Create a new issue if your problem isn't already listed

