# Custom Movie Recommender System

This project provides a personalized movie recommendation service, utilizing a powerful backend built with H2O Wave and an interactive frontend created with Streamlit. It leverages movie data and similarity models to offer recommendations, fetching movie posters dynamically through The Movie Database (TMDb) API.

## Features

- Personalized movie recommendations.
- Dynamic retrieval of movie posters from TMDb.
- Responsive design accommodating various screen sizes.
- User-friendly interfaces for both H2O Wave and Streamlit applications.

## Preview

### Streamlit App Preview

Watch the Streamlit app in action here: [Streamlit App Preview](<https://github.com/isurulkh/Movie-Recommender-System_using_h2o-wave/blob/cc000b1a79ad4155defa0744b5d0508390786ed7/demo%20videos/Steamlite.mkv>)

### H2O Wave App Preview

Check out the H2O Wave app here: [H2O Wave App Preview](<[demo videos/Waveapp.mkv](https://github.com/isurulkh/Movie-Recommender-System_using_h2o-wave/blob/63dc9ac4f10d2be7c16958294c770d2113c7f382/demo%20videos/Waveapp.mkv)>)

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- Virtual environment setup for Python.
- An API key from [The Movie Database (TMDb)](https://developers.themoviedb.org/3/getting-started/introduction).

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/isurulkh/Movie-Recommender-System_using_h2o-wave.git
```

2.**Create a virtual environment:**

```bash
python -m venv venv

```
3.**Create a virtual environment:**

**Windows**
```bash
.\venv\Scripts\activate
```

**Mac**
```bash
source venv/bin/activate
```

4.**Install dependencies:**

```bash
pip install -r requirements.txt

```

### Downloading Models Manually

Before running the applications, you need to download the necessary model files manually and place them in the `Models` folder within your project directory. Follow the steps below:

1. **Create a `Models` folder in your project directory** if it does not already exist.

2. **Download the model files** from the following Google Drive links:
   - Model Files: [Download Link](https://drive.google.com/file/d/1csjCuVtLILvv-AfGzwgl_G4jnkkuV8vD/view?usp=drive_link](https://drive.google.com/drive/folders/1pmRVtDOvgXBaElzXPYxVsAUNMGxzS1Iu?usp=sharing)).

3. **Move the downloaded files to the `Models` folder.**

Ensure all model files are correctly placed in the `Models` folder before proceeding to run the applications.

### Running the Applications

After setting up the environment and downloading the necessary model files, you are ready to run the applications.

#### H2O Wave Application

1. **Start the H2O Wave Server:** Navigate to your project directory in the terminal, ensure your virtual environment is activated, and run the following command:
   ```bash
   wave run app.py
   ```
**This command starts the H2O Wave server and serves your application.**

👉Access the Application: Open a web browser and navigate to http://localhost:10101/demo to interact with the H2O Wave application. You should see the interface for selecting movies and receiving recommendations.


#### Streamlit Application

👉Run the Streamlit App: In a new terminal window or tab, navigate to your project directory, activate the virtual environment, and execute the following command:
 ```bash
streamlit run streamlitapp.py
 ```


#### Usage
 **H2O Wave Application**
 
👉Select a Movie: Use the dropdown menu to choose a movie you like or are interested in.
👉Get Recommendations: Click the "Show Recommendations" button to see a list of recommended movies based on your selection. The recommendations will include movie posters and titles.


**Streamlit Application**

👉Movie Selection: Similar to the H2O Wave app, start by selecting a movie from the dropdown list.
👉Viewing Recommendations: After selecting a movie, the app will display a list of recommended movies, including their posters and additional details, depending on the app's design.


👉Both applications leverage the same underlying model for recommendations but offer different user interfaces and experiences. You can explore both to see which one you prefer or to compare their functionalities.
