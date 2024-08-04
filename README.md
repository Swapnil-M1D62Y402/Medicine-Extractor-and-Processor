# Medicine-Extractor-and-Processor

General Purpose Text Extractor with Drug Named Entity Recognition with Gemini Large Language Model and spaCy library
This project explores the use of Gemini Large Image Model's Optical Character Recognition (OCR) capabilities and spaCy, a powerful Python library for Natural Language Processing (NLP), to develop a drug named entity recognition (NER) system.

Project Overview
The core functionality of this project lies in leveraging Gemini's ability to extract text from images containing drug information and spaCy's NER models to identify and classify drug mentions within the extracted text. This approach offers a potential solution for tasks like:

Automating drug information extraction from medical documents (e.g., prescriptions, discharge summaries)
Supporting information retrieval systems in the medical domain
Facilitating drug discovery and pharmacovigilance efforts
Dependencies
This project relies on the following external libraries:

geminilm (for interfacing with Gemini Large Language Model)
spacy (for named entity recognition)
(Optional) Libraries for data manipulation (e.g., pandas) and visualization (e.g., matplotlib)
Note: Installation instructions for these libraries can be found in their respective documentation.

Usage
Clone this repository:

Bash
>git clone https://https://github.com/Swapnil-M1D62Y402/Medicine-Extractor-and-Processor

Install dependencies:

Bash
>pip install -r requirements.txt

The project structure should include a Python script implementing the OCR and NER functionality. Refer to the script's documentation within the code for specific execution instructions. This might involve providing paths to image files or datasets containing drug information.

##Example
The script is expected to output the identified drug mentions along with their corresponding classifications (e.g., brand names, generic names). Here's a fictional illustration:

![Output-1](https://github.com/user-attachments/assets/34122886-e383-4dfd-8344-286b93a2aa88)

![Output-2](https://github.com/user-attachments/assets/e320ed34-b66d-463a-973a-4513830bd547)

![Output-3](https://github.com/user-attachments/assets/0eb86731-ed31-4d0a-b5e8-de2d3ed4f3f3)


Some of the user prompts used to improve the extraction process are as of following

https://github.com/Swapnil-M1D62Y402/Medicine-Extractor-and-Processor/blob/main/prompts.txt

*prompt-1* - converts text to json format and label the fields
>convert the image to text and format it into json 

*prompt-2* - converts text to json format and beautify it
>convert the image to text and format it into json and beautify it.  

*prompt-3* - converts text to json format and beautify it and separates the medicine from other fields
>convert the image to text to json format and beautify it. If possible then extract the medicine names from it and name the key value medicine.

This project serves as a starting point for exploring the potential of Gemini and spaCy for drug NER tasks. You can extend this work by:

Training custom spaCy models for improved drug mention classification accuracy
Integrating the NER system with a larger application (e.g., information retrieval system)
Experimenting with different Gemini OCR configurations for optimal text extraction
Contributing

I welcome contributions to this project! Feel free to submit pull requests with improvements, bug fixes, or additional functionalities.
