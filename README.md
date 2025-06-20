# Animacy Annotation & Classification

This repository contains a Jupyter Notebook that is part of a teaching concept for automatic and manual annotation of animate entities in German texts. It compares machine learning-based and manual annotation and evaluates a classifier using precision, recall, and F1 score. The manual annotations are loaded using the [gitma package](https://github.com/forTEXT/gitma). 

The underlying code is based on the project **“Animacy in German Folktales”**:  
**Häußler, J., von Keitz, J., Gius, E. (2024).** Animacy in German Folktales. CHR 2024: Computational Humanities Research Conference, December 4–6, 2024, Aarhus, Denmark.
[Paper](https://ceur-ws.org/Vol-3834/paper90.pdf) | [GitHub Repository](https://github.com/forTEXT/Animacy_in_German_Folktales)


## 📂 Contents
- **`animacy_annotation.ipynb`** – Main notebook for annotation and evaluation.
- **`models/`** – Pre-trained classifier and vectorizer
- **`features/`** – Classes for feature extraction
- **`catma/`** – Manual annotations exported from Catma using the gitma package.


## 🚀 Usage
### Using the Docker container

This repository can be used directly in a Docker container.
This requires **Docker**.

1. **Install Docker**
   If Docker is not yet installed, download it here and install it:
🔗 [Download Docker](https://docs.docker.com/get-docker/)  

2. **Download Docker image**
   
   The prepared image is available on **Docker Hub**. To load it, run the following command:
```sh
   docker pull janis711/animacy-annotation-course:latest
   ```
3. **Start Docker container**
```sh
   docker run -p 8888:8888 janis711/animacy-annotation-course
   ```
4. **Open Jupyter Notebook**
   
   After starting, Docker outputs a Jupyter Notebook URL (e.g.: `http://127.0.0.1:8888/...`). Open this link in your browser and open the notebook animacy_annotation.ipynb.

5. **Stop container**
   
   After use, the Docker container can be stopped again:
   ```sh 
   docker ps  # Displays running containers
   docker stop CONTAINER_ID
   ```

### Local installation
**Requirements**:
* Python version 3.9.* installed (not 3.10 if Gitma is to be used)
* Jupyter Notebook installed
1. **Clone the repository and change to the appropriate directory**
   ```
   git clone https://github.com/janis711/animacy-classification-course.git
   cd animacy-classification-course
   ```
   If Git is not installed, the code can be downloaded as a ZIP file from GitHub:
   * Click on “Code” and select “Download ZIP”
   * Unzip the file and change to the unzipped directory
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. Install the gitma Python package
   ```
   pip install git+https://github.com/forTEXT/gitma
   ```
4. Start Jupyter Notebook
   ```
   jupyter notebook
   ```
5. Open and run `animacy_annotation.ipynb`.


