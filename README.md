# Animacy Annotation & Classification

Dieses Repository enthält ein Jupyter Notebook, das Teil eines Lehrkonzepts zur automatischen und manuellen Annotation belebter Entitäten in deutschen Texten ist. Es vermittelt den Vergleich zwischen Machine-Learning-gestützter und manueller Annotation sowie die Evaluierung eines Classifiers anhand von Precision, Recall und F1-Score. Die manuellen Annotationen werden mit dem [gitma Package](https://github.com/forTEXT/gitma) geladen. 

Der zugrundeliegende Code basiert auf dem Projekt **"Animacy in German Folktales"**:  
**Häußler, J., von Keitz, J., Gius, E. (2024).** Animacy in German Folktales. CHR 2024: Computational Humanities Research Conference, December 4 – 6, 2024, Aarhus, Denmark.  
[Paper](https://ceur-ws.org/Vol-3834/paper90.pdf) | [GitHub Repository](https://github.com/forTEXT/Animacy_in_German_Folktales)


## 📂 Inhalt
- **`animacy_annotation.ipynb`** – Haupt-Notebook zur Annotation und Evaluation.
- **`models/`** – Vortrainierter Classifier und Vektorisierer
- **`features/`** - Klassen für die Feature Extraktion
- **`catma/`** - Manuelle Annotationen, die mit dem gitma Package aus Catma exportiert wurden.   


## 🚀 Nutzung
### Nutzung in Binder (ohne lokale Installation)

### Lokale Installation
**Voraussetzungen**:
* Python Installation in Version 3.9 (nicht 3.10, wenn Gitma verwendet werden soll)
* Jupyter Notebook Installation
1. **Repository klonen und in das entsprechende Verzeichnis wechseln**  
   ```
   git clone https://github.com/dein-user/animacy-annotation.git
   cd animacy-annotation
   ```
   Falls Git nicht installiert ist, kann der Code als ZIP-Datei von GitHub heruntergeladen werden:
   * Gehe zu GitHub Repository
   * Klicke auf "Code" und wähle "Download ZIP"
   * Entpacke die Datei und wechsle in das entpackte Verzeichnis
2. **Abhängigkeiten installieren**
   ```
   pip install -r requirements.txt
   ```
3. **Zusätzliche Abhängigkeiten über postBuild installieren**
    ```
    bash postBuild
    ```
4. Jupyter Notebook starten
    ```
    jupyter notebook
    ```

5. Das gitma Python Package installieren
   ```
   pip install git+https://github.com/forTEXT/gitma
   ```
6.  `animacy_annotation.ipynb` öffnen und ausführen.
