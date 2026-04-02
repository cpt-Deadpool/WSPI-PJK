# WSPI-PJK
ML Project CS 5821

This project's goal is to classify images of road surfaces into categories based on road conditions

Categories: 
- Dry 
- Packed snow 
- Mixed snow over ice 
- Ice

This specific implementation is to train the model from scratch as normal, but to also experiment with the viability of using Google Colab to run and train the model. 

## How to run 
**Google Colab:**
1. Open Google Colab and open the file there
2. In the toolbar go Runtime > Change Runtime Type > T4 Gpu (or any other gpu)
3. When prompted, allow Google Drive access for mounting
4. Scan through the code and edit file paths as needed
5. Run the cells in order and according to the comments

**Local (Keep in mind this is untested):**
1. Download the libraries and setup an enviorment:
    - **Windows**: Run the `setup.bat` file to setup a enviorment and install the needed packages to it
    - **Mac/Linux**: Run `bash setup.sh` in the terminal from the project directory.
2. Start the enviorment:
    - **Windows**: Run `venv\Scripts\activate` to start the enviorment
    - **Max/Linux**: Run `source venv/bin/activate` to start the enviorment
3. In your editor, select the venv as your Python interpreter/kernel (look for the path containing `venv`)
4. Scan through the code and edit file paths as needed
5. Run the notebook cells in order and according to the comments.



*Credits: Jordan Johnson*
