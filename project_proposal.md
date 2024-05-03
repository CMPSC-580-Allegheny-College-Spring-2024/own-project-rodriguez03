# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

This document is to contain your project proposal. __As you complete each of the below sections in this document, please be sure to remove all preamble text so that it does not appear in your work.__

## GitHub Handle: rodriguez03

## Name: Sabrina Rodriguez

## Major: CS

## Project Title: Prediciting District Maps 

---

## Introduction

This project aims to analyze different districts within the state of Pennsylvania to predict future election outcomes. Inspired by researching redistricting and gerrymandering within the state of PA, there are many factors that play into election outcomes. To address this question, the project harnesses a diverse array of databases containing information on partisan voting patterns across districts, demographic profiles, socioeconomic indicators, and candidate profiles spanning the period from 2012 to 2022.

Understanding how diverse segments of the population, with their distinct circumstances, sway towards particular candidates is crucial in deciphering electoral trends accurately. By delving into the intricacies of gerrymandering and its implications, I plan to uncover the roles played by various factors in shaping electoral landscapes. Ultimately, the central research question driving this is to discern the primary factors dictating an accurate prediction of election maps for Pennsylvania.

This project fills a significant gap in the current understanding of electoral dynamics by offering an exploration of the factors that influence election outcomes in Pennsylvania. By addressing this gap, the research aims to contribute valuable insights to the field, informing future discussions and strategies aimed at promoting fair and representative electoral processes.

In addition to leveraging diverse databases to analyze Pennsylvania's electoral landscape, this project utilizes advanced visual data strategies, including Leaflet. Through the integration of Leaflet and other visual data strategies, this project seeks to enhance accessibility and understanding of the complexities of elections. By presenting data in interactive and visually compelling formats, I can effectively communicate findings to a broad audience, including policymakers, researchers, and the general public. This approach not only enhances the project's analytical capabilities but also fosters transparency and accountability in electoral processes.

## Literature Review

TODO (10 source minimum, with 5 of those being published peer-reviewed articles): Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further (in detail) contributes to the `why is the project important?` question.

Gerrymandering, a practice involving the manipulation of district boundaries to gain political advantage, undermines the representation of constituents by distorting voting outcomes. Its prevalence in Pennsylvania has drawn considerable attention, motivating a closer examination of its impact on electoral dynamics within the state. One notable instance is highlighted by Cervas and Grofman (2020), who discuss how the Pennsylvania Supreme Court invalidated a congressional map drawn by Republicans in 2011 due to significant partisan gerrymandering. Following this decision, the court intervened by implementing its own map for the 2018 elections after the state failed to devise a suitable replacement. Through a comparative analysis of the 2011 and 2018 maps, as well as examination of proposed remedy maps from both Republican legislators and the Democratic governor, the article reveals the overtly pro-Republican nature of the 2011 map. Furthermore, it suggests that while the Republican-proposed remedy map retained a covert pro-Republican bias, the Democratic governor's proposal exhibited a slight pro-Republican tilt. In contrast, the court-drawn 2018 remedial map was found to be free from gerrymandering according to various metrics. Such instances serve as compelling motivations for projects like this one, which seek to forecast election outcomes in different districts, thereby capturing shifts in voting majorities over a decade of redistricting and electoral cycles.

## Prototype

In this project, the goal is to develop an interactive visualization tool to explore Pennsylvania's electoral landscape at the district level. The main objective is to provide stakeholders, including policymakers and the general public, with insights into the distribution of partisan support across different districts within the state. To achieve this goal, I leveraged PyQt5, a Python library for creating graphical user interfaces, to build a user-friendly application that displays a map of Pennsylvania with district boundaries and corresponding electoral data. The core of this application is a Qt QMainWindow subclass called PennsylvaniaMap, which serves as the main window for the application. The setup_ui method of this class, it generates HTML content dynamically using string formatting techniques to embed Leaflet.js, a popular JavaScript library for interactive maps, into our application. This HTML content includes a map element with an embedded Leaflet map initialized to display Pennsylvania at an appropriate zoom level. Furthermore, utilizing the QWebEngineView widget provided by PyQt5 to render the dynamically generated HTML content within the application. This widget allows us to display the interactive map directly within the PyQt5 application window. Additionally, writing the generated HTML content to a file named "pennsylvania_map.html" for archival purposes and open this file in the default web browser using the webbrowser module to provide users with an alternative viewing option. Overall, this project combines the power of Python for backend logic and PyQt5 for front-end GUI development to create an interactive visualization tool that facilitates the exploration and understanding of Pennsylvania's electoral dynamics. With this application, users can interactively analyze and interpret electoral data at the district level, thereby gaining valuable insights into the political landscape of the state.

The core of this application is a Qt QMainWindow subclass called PennsylvaniaMap, which serves as the main window for the application. The setup_ui method of this class generates HTML content dynamically using string formatting techniques to embed Leaflet.js, a popular JavaScript library for interactive maps, into our application. This HTML content includes a map element with an embedded Leaflet map initialized to display Pennsylvania at an appropriate zoom level. 

```python
class PennsylvaniaMap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pennsylvania Map")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        # HTML content generation
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pennsylvania Map with Districts</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <style>
            #map { height: 600px; }
        </style>
        </head>
        <body>
        <div id="map"></div>

        <script>
            // Integrating Leaflet.js
        </script>
        </body>
        </html>
        """

        # Creating the QWebEngineView widget and loading HTML content
        self.map_widget = QWebEngineView(self)
        self.map_widget.setHtml(html_content, QUrl.fromLocalFile(""))
        self.map_widget.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(self.map_widget)
```

Here's an overview of the resources and methods in this project:

1. **Design of the Algorithm**: The algorithmic aspect of this project involves designing the logic for generating dynamic HTML content that embeds Leaflet.js for interactive map rendering. This algorithm is implemented within the `setup_ui` method of the `PennsylvaniaMap` class.

2. **Data Collection Methods**: Data collection methods are not explicitly addressed in this project, as it primarily focuses on visualization rather than data analysis. However, in a real-world scenario, data collection methods would involve gathering electoral data, including voting patterns and district boundaries, from reliable sources such as government databases or research institutions.

3. **Applied Software Libraries**: The project heavily relies on the PyQt5 library for creating the graphical user interface and integrating web content within the application window. Additionally, Leaflet.js is utilized for interactive map visualization. Other standard Python libraries such as `os`, `sys`, and `webbrowser` are used for file manipulation and web browsing functionalities.

4. **Required Tools**: The essential tools for this project include a Python interpreter (version 3.x), a text editor or integrated development environment (IDE) for writing code, and a web browser for viewing the generated HTML content.

5. **Types of Statistical Analyses and Models**: Since this project is focused on visualization rather than statistical analysis, there are no specific statistical analyses or models applied. However, future extensions of this project could involve incorporating statistical techniques for analyzing electoral data and predicting voting patterns.

## Preliminary Results and Outcomes

One significant outcome is the ability of the application to dynamically generate HTML content embedding an interactive map using Leaflet.js. This allows users to visualize district boundaries and corresponding electoral data directly within the PyQt5 application window. Additionally, the application writes the generated HTML content to a file for archival purposes and opens it in the default web browser, providing users with an alternative viewing option. The application's capability to open the generated HTML file in the default web browser enhances its accessibility and usability. Users can interact with the electoral map both within the application window and in their preferred web browser, offering flexibility in viewing and analyzing electoral data. Overall, the outcome of the project demonstrates the successful integration of Python backend logic with PyQt5 frontend GUI development to create an interactive visualization tool. With its capabilities and applications, the tool facilitates the exploration and understanding of Pennsylvania's electoral dynamics, empowering users to gain valuable insights into the political landscape of the state.

## Conclusions and Future Work

TODO: Summarize your work and outline future steps needed to complete to take the project to the next stage (for example, if you were to continue with this project in 600/610). You must also address ethical implications of your project, especially as pertains to the public release or use of your software or methods.

To effectively complete this project, it's crucial to ensure the code can efficiently read and process the extensive datasets encompassing polling results and electoral statistics spanning the years 2012 to 2022. This involves implementing robust algorithms for data parsing and manipulation, as well as establishing reliable data structures to store and organize the retrieved information. Furthermore, the development process requires the integration of advanced predictive modeling techniques, such as the confusion matrix method, to analyze the historical data and generate accurate forecasts for future election outcomes at the district level. This entails designing and implementing algorithms capable of training predictive models using the available data and evaluating their performance to ensure their reliability and accuracy. While these technical aspects constitute challenges, another critical aspect of the project involves creating an intuitive user interface that enables stakeholders to interact with the electoral data effectively. This involves designing user-friendly features and visualizations that facilitate data exploration and interpretation, empowering users to gain valuable insights into Pennsylvania's electoral dynamics. Additionally, the project necessitates an understanding of geographical information systems (GIS) and mapping technologies to accurately represent electoral boundaries and visualize electoral data on a map of Pennsylvania. This involves leveraging libraries and tools capable of rendering interactive maps and overlaying electoral information, such as polling results and demographic data, onto the map interface. By addressing these challenges, the project will deliver a sophisticated and informative electoral analysis tool that provides valuable insights into Pennsylvania's political landscape.

## References

TODO: Add references in the [ACM style](https://www.acm.org/publications/authors/reference-formatting). All references must be cited in the proposal.


- Beauxis-Aussalet, E., & Hardman, L. (2014). Visualization of confusion matrix for non-expert users. In IEEE Conference on Visual Analytics Science and Technology (VAST)-Poster Proceedings (pp. 1-2).
- Cervas, J. R., & Grofman, B. (2020). Tools for identifying partisan gerrymandering with an application to congressional districting in Pennsylvania. Political Geography, 76, 102069.
- Fachrie, M., & Ardiani, F. (2021). Predictive Model for Regional Elections Results based on Candidate Profiles. In 2021 8th International Conference on Electrical Engineering, Computer Science and Informatics (EECSI) (pp. 247-252). IEEE.
- Liang, J. (2022). Confusion matrix: Machine learning. POGIL Activity Clearinghouse, 3(4).
- Richardson, B., & Hougen, D. F. (2020). Districts by demographics: Predicting US house of representative elections using machine learning and demographic data. In 2020 19th IEEE International Conference on Machine Learning and Applications (ICMLA) (pp. 833-838). IEEE.
- Wickham, H. (2014). Tidy data. Journal of Statistical Software, 59(10), 1-23. Retrieved from https://vita.had.co.nz/papers/tidy-data.pdf
- W3Schools. (n.d.). Python - Machine Learning - Confusion Matrix. Retrieved from https://www.w3schools.com/python/python_ml_confusion_matrix.asp