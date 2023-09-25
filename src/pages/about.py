"""About page layout."""
# pylint: disable=wrong-import-position
# flake8: noqa: E402
import os
import sys
import dash_bootstrap_components as dbc
from dash import html

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


urls = {
    "github": "https://github.com/rokobo",
    "linkedin": "https://www.linkedin.com/in/pedrokobori/"
}

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(dbc.CardBody([
                html.H1("Hello! 👋, My name is Pedro Kobori",
                        style={"textAlign": "start"}),
                html.Br(),
                html.H4("Self-taught developer with a passion for databases, \
                        productivity software, automations and data analysis.",
                        style={"textAlign": "start"})
            ]), class_name="about-card")
        ], class_name="d-flex flex-column justify-content-center"),
        dbc.Col([
            dbc.Row(html.A([html.Img(
                src="assets/github.png", className="home-icons"
            )], href=urls["github"], target="_blank")),
            dbc.Row(html.A([html.Img(
                src="assets/linkedin.png", className="home-icons"
            )], href=urls["linkedin"], target="_blank")),
        ], width="auto", class_name="d-flex flex-column \
            justify-content-between align-items-center")
    ], class_name="about-first-row"),
    dbc.Row([
        dbc.Card(dbc.CardBody(html.H5("""
            I am self-taught backend software developer. My education is based 
            on the curriculum dictated by the Open Source Society University.
        """)), class_name="sub-about-card"),
        html.Br(),
        dbc.Card(dbc.CardBody(html.H5("""
            I always loved hoarding and analyzing all kinds of data. Throughout
            life, this lead me to recording and thinking about every piece
            of information I could get my hands on. I became particularly
            interested in automating data analysis and collection, as well
            as in how information is perceived and understood by people. I
            find it fascinating how people, with their own experiences,
            produced vastly different theories and conclusions with the
            information they are surrounded by. This eventually made me
            become interested in computer software development, psychology, 
            market analysis and the dynamics of data."
        """)), class_name="sub-about-card"),
        html.Br(),
        dbc.Card(dbc.CardBody(html.H5("""
            To me, learning about data analysis is more than a mathematical 
            problem. Learning to gather and interpret data served me well 
            in numerous situations. By applying the knowledge I gained 
            from constantly trying to find patterns in data, I was able to 
            make better decisions in life. Information is everywhere, 
            training to interpret patterns and biases enables one to 
            become a better person.
        """)), class_name="sub-about-card"),
        html.Br(),
        dbc.Card(dbc.CardBody(html.H5("""
            I believe the study and analysis of data is a fundamental pilar 
            for the development of a better world. Being able to transform 
            data into meaningful and helpful insights is what I strive for 
            as a software developer.
        """)), class_name="sub-about-card")
    ], class_name="about-second-row")
])
