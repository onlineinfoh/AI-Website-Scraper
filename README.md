This is a small project that I have being doing for a few days.

This app uses **streamlit** for website structure, **selenium** to extract website information, **beautifulsoup** to clean and format website HTML information, and lastly **llama3.2:1b** model to provide the summary functionality. 

One of the cons for this app in terms of performance is the speed of the model: I only have a laptop with **no powerful GPUs like CUDA**, and I have to use a relatively less trained Ollama model, which results in that the summarizer feature of this app is not practical and **quite inaccurate given more information**. 