1.Prerequisites:
Before running the app, make sure you have the following installed:
Python 3.7 or later

2.Setup:
2.1->Create a virtual environment (optional but recommended):
      ->python -m venv venv
        # Activate the virtual environment
        # Windows
        ->venv\Scripts\activate
        # macOS/Linux
        source venv/bin/activate

2.2->Install the required dependencies: pip install -r requirements.txt

2.3->Create a .env file in the project root and add your OPENAI API key:
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE

2.4->Running the App :To run the app locally, execute the following command:
        streamlit run app.py

(The app will open in your default web browser.)



3.Usage:
-Upload PDF Files: Click on the "Upload your PDF Files" button in the sidebar and select one or more PDF files.

-Ask a Question: Enter your question in the "Ask a Question from the PDF Files" text box and click "Submit & Process".

-Chat with OPENAI: The app will process the PDF files and then use the Gemini API to answer your question based on the uploaded PDF content.

4.Features:
-Upload multiple PDF files.
-Chat with the OPENAI API to get answers from the PDF content.
-Error handling for incorrect questions or missing context.

5.Contributing:
Contributions are welcome! If you'd like to add new features, improve existing ones, or fix any issues, please follow these steps:
-Fork the repository.
-Create a new branch.
-Make your changes.
-Commit your changes.
-Push to the branch.
-Create a new Pull Request.