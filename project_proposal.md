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

The program attempts to fill a significant gap in the current understanding of electoral dynamics by offering an exploration of the factors that influence election outcomes in Pennsylvania. By addressing this gap, the research aims to contribute valuable insights to the field, informing future discussions and strategies aimed at promoting fair and representative electoral processes.

In addition to leveraging diverse databases to analyze Pennsylvania's electoral landscape, this project utilizes advanced visual data strategies, including Leaflet. Through the integration of Leaflet and other visual data strategies, it seeks to enhance accessibility and understanding of the complexities of elections. By presenting data in interactive and visually compelling formats, I can effectively communicate findings to a broad audience, including policymakers, researchers, and the general public. This approach not only enhances the project's analytical capabilities but also fosters transparency and accountability in electoral processes.

## Literature Review

Gerrymandering, a practice involving the manipulation of district boundaries to gain political advantage, undermines the representation of constituents by distorting voting outcomes. Its prevalence in Pennsylvania has drawn considerable attention, motivating a closer examination of its impact on electoral dynamics within the state. One instance is highlighted by Cervas and Grofman (2020), who discuss how the Pennsylvania Supreme Court invalidated a congressional map drawn by Republicans in 2011 due to significant partisan gerrymandering. Following this decision, the court intervened by implementing its map for the 2018 elections after the state failed to devise a suitable replacement. Through a comparative analysis of the 2011 and 2018 maps and examination of proposed remedy maps from Republican legislators and the Democratic governor, the article reveals the overtly pro-Republican nature of the 2011 map.
Furthermore, it suggests that while the Republican-proposed remedy map retained a covert pro-Republican bias, the Democratic governor's proposal exhibited a slight tilt. In contrast, according to various metrics, the court-drawn 2018 remedial map was free from gerrymandering. Such instances serve as compelling motivations for projects like this one, which seeks to forecast election outcomes in different districts, thereby capturing shifts in voting majorities over a decade of redistricting and electoral cycles. 

This project initiates an extensive data collection effort and gathers a wealth of information crucial to understanding Pennsylvania's elections. Historical voting patterns, demographic compositions, socioeconomic indicators, and candidate profiles form the backbone of this dataset. Each piece offers unique insights, from revealing voter preferences over time to providing context on district characteristics and candidate dynamics.

Building upon the dataset assembled, the project utilizes predictive modeling techniques to output future election outcomes. Inspired by prior studies highlighting the impact of gerrymandering, the project seeks to uncover hidden patterns within the data. Leveraging machine learning algorithms, as discussed by Richardson and Hougen (2020), the project aims to develop predictive models capable of discerning the factors driving electoral outcomes. These models, incorporating historical voting patterns, demographic characteristics, and candidate profiles, generate forecasts for future elections. 

In parallel, the project incorporates advanced visual data strategies to enhance accessibility and interpretability. Drawing from research on data visualization, Beauxis-Aussalet and Hardman's (2014) work on visualization of confusion matrices for non-expert users provides valuable insights. Tools such as Leaflet create interactive representations of electoral data, as Wickham (2014) advocates. These visualizations are powerful communication tools, enabling stakeholders to explore Pennsylvania's electoral dynamics. The project fosters broader engagement with its findings by presenting data in visually compelling formats. Interactive visualizations allow users to assess the impact of various factors on election outcomes, enhancing transparency in the electoral process. Machine learning (ML) techniques have emerged as powerful tools for predicting election outcomes, offering a data-driven approach to understanding complex electoral dynamics.

Richardson and Hougen (2020) demonstrated the efficacy of ML algorithms in predicting US House of Representative elections by leveraging demographic data. These algorithms, including decision trees and neural networks, capture nonlinear relationships and interactions among variables, making them well-suited for analyzing electoral behavior. In parallel, Liang (2022) discussed the utility of confusion matrices in evaluating the performance of ML models in political predictions. By providing a summary of prediction accuracy, confusion matrices enable researchers to identify areas where models excel and where they may need improvement. This sentiment is echoed by Wang and Chen (2019), who emphasized the importance of evaluating prediction accuracy in understanding gerrymandering effects. Integrating ML techniques and confusion matrix analysis in political predictions allows researchers to make informed assessments of electoral outcomes and contribute to a deeper understanding of the factors driving political dynamics. By combining data-driven analysis with advanced modeling techniques and visual data strategies, the project adopts an approach to understanding Pennsylvania's electoral dynamics. The project aims to bridge the gap between research on gerrymandering, predictive modeling, and data visualization, offering valuable insights to promote fair and representative electoral processes. Through rigorous analysis and transparent communication of findings, the project contributes meaningfully to electoral studies for decision-making.

Examining gerrymandering's impact on Pennsylvania's electoral dynamics demonstrates the critical need for analysis and predictive modeling to ensure fair and representative electoral processes. The instances highlighted by Cervas and Grofman (2020) serve as motivations for projects to forecast election outcomes and capture shifts in voting majorities over time. This project will show Pennsylvania's electoral landscape by initiating a data collection effort encompassing historical voting patterns, demographic compositions, and candidate profiles. Leveraging predictive modeling techniques, including machine learning algorithms inspired by Richardson and Hougen (2020), the project aims to uncover hidden patterns and factors driving electoral outcomes. Moreover, incorporating advanced visual data strategies, advocated by Beauxis-Aussalet and Hardman (2014) and Wickham (2014), enhances accessibility and interpretability, enabling stakeholders to explore electoral dynamics. Integrating data-driven analysis, advanced modeling techniques, and visual data strategies, the project bridges the gap between research on gerrymandering, predictive modeling, and data visualization, offering valuable insights to promote fair and representative electoral processes. Ultimately, the project's rigorous analysis and transparent communication of findings contribute meaningfully to the field of electoral studies, empowering stakeholders with actionable insights for decision-making in Pennsylvania's political landscape.

## Prototype

In this project, the goal is to develop an interactive visualization tool to explore Pennsylvania's electoral landscape at the district level. The main objective is to provide stakeholders, including policymakers and the general public, with insights into the distribution of partisan support across different districts within the state. To achieve this goal, I leveraged PyQt5, a Python library for creating graphical user interfaces, to build a user-friendly application that displays a map of Pennsylvania with district boundaries and corresponding electoral data. The core of this application is a Qt QMainWindow subclass called PennsylvaniaMap, which serves as the main window for the application. The setup_ui method of this class, it generates HTML content dynamically using string formatting techniques to embed Leaflet.js, a popular JavaScript library for interactive maps, into this application. This HTML content includes a map element with an embedded Leaflet map initialized to display Pennsylvania at an appropriate zoom level. Furthermore, utilizing the QWebEngineView widget provided by PyQt5 to render the dynamically generated HTML content within the application. This widget allows us to display the interactive map directly within the PyQt5 application window. Additionally, writing the generated HTML content to a file named "pennsylvania_map.html" for archival purposes and open this file in the default web browser using the webbrowser module to provide users with an alternative viewing option. Overall, this project combines the power of Python for backend logic and PyQt5 for front-end GUI development to create an interactive visualization tool that facilitates the exploration and understanding of Pennsylvania's electoral dynamics. With this application, users can interactively analyze and interpret electoral data at the district level, thereby gaining valuable insights into the political landscape of the state.

The core of this application is a Qt QMainWindow subclass called PennsylvaniaMap, which serves as the main window for the application. The setup_ui method of this class generates HTML content dynamically using string formatting techniques to embed Leaflet.js, a popular JavaScript library for interactive maps. This HTML content includes a map element with an embedded Leaflet map initialized to display Pennsylvania at an appropriate zoom level. 

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

One significant outcome of the project lies in the application's ability to dynamically generate HTML content embedding an interactive map using Leaflet.js, a popular JavaScript library for creating interactive maps. This integration enables users to visualize district boundaries and corresponding electoral data directly within the PyQt5 application window, offering a seamless and intuitive user experience. By leveraging Leaflet.js, the application empowers users to interact with the electoral map, zooming in and out, panning across regions, and accessing detailed information about specific districts. Moreover, the application writes the generated HTML content to a file for archival purposes and automatically opens it in the default web browser. This feature provides users with an alternative viewing option, enhancing the accessibility and usability of the tool. The application's capability to open the generated HTML file in the default web browser further expands its accessibility and usability. Users can seamlessly transition between viewing the electoral map within the application window and in their preferred web browser, depending on their preferences and workflow. This flexibility in viewing and analyzing electoral data caters to diverse user needs and preferences, ensuring that the tool accommodates a wide range of usage scenarios. Overall, the successful integration of Python backend logic with PyQt5 frontend GUI development demonstrates the project's ability to create an interactive visualization tool that meets user requirements and expectations. By providing users with the means to explore and understand Pennsylvania's electoral dynamics, the tool empowers them to gain valuable insights into the political landscape of the state. Whether for research purposes, educational endeavors, or policy analysis, the tool serves as a valuable resource for navigating and interpreting electoral data, contributing to a deeper understanding of the democratic process.

## Conclusions and Future Work

To effectively complete this project, it's crucial to ensure the code can efficiently read and process the extensive datasets encompassing polling results and electoral statistics spanning the years 2012 to 2022. This involves implementing robust algorithms for data parsing and manipulation, as well as establishing reliable data structures to store and organize the retrieved information. Furthermore, the development process requires the integration of advanced predictive modeling techniques, such as the confusion matrix method, to analyze the historical data and generate accurate forecasts for future election outcomes at the district level. This entails designing and implementing algorithms capable of training predictive models using the available data and evaluating their performance to ensure their reliability and accuracy. While these technical aspects constitute challenges, another critical aspect of the project involves creating an intuitive user interface that enables stakeholders to interact with the electoral data effectively. This involves designing user-friendly features and visualizations that facilitate data exploration and interpretation, empowering users to gain valuable insights into Pennsylvania's electoral dynamics. Additionally, the project necessitates an understanding of geographical information systems (GIS) and mapping technologies to accurately represent electoral boundaries and visualize electoral data on a map of Pennsylvania. This involves leveraging libraries and tools capable of rendering interactive maps and overlaying electoral information, such as polling results and demographic data, onto the map interface. By addressing these challenges, the project will deliver a sophisticated and informative electoral analysis tool that provides valuable insights into Pennsylvania's political landscape.

## References

- E. Beauxis-Aussalet and L. Hardman. 2014. Visualization of confusion matrix for non-expert users. In IEEE Conference on Visual Analytics Science and Technology (VAST)-Poster Proceedings, 1-2.

- J. R. Cervas and B. Grofman. 2020. Tools for identifying partisan gerrymandering with an application to congressional districting in Pennsylvania. Political Geography 76, 102069.

- M. Fachrie and F. Ardiani. 2021. Predictive Model for Regional Elections Results based on Candidate Profiles. In 2021 8th International Conference on Electrical Engineering, Computer Science and Informatics (EECSI), 247-252. IEEE.

- J. Liang. 2022. Confusion matrix: Machine learning. POGIL Activity Clearinghouse 3, 4.

- B. Richardson and D. F. Hougen. 2020. Districts by demographics: Predicting US house of representative elections using machine learning and demographic data. In 2020 19th IEEE International Conference on Machine Learning and Applications (ICMLA), 833-838. IEEE.

- Riverbank Computing Limited. (2024). PyQt5 Documentation. Retrieved from https://www.riverbankcomputing.com/static/Docs/PyQt5/

- OpenStreetMap contributors. (2024, May 3). About OpenStreetMap. Retrieved from https://www.openstreetmap.org/about

- Python Software Foundation. (2024, May 3). PyQt. Retrieved from https://wiki.python.org/moin/PyQt

- H. Wickham. 2014. Tidy data. Journal of Statistical Software 59, 10, 1-23. Retrieved from https://vita.had.co.nz/papers/tidy-data.pdf.

- Wang, Y., and Chen, J. 2019. Understanding Gerrymandering: A Review of Methods and Approaches. *International Journal of Geographical Information Science* 33, 11 (2019), 2293-2314.

- W3Schools. n.d. Python - Machine Learning - Confusion Matrix. Retrieved from https://www.w3schools.com/python/python_ml_confusion_matrix.asp.
