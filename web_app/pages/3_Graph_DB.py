# Import necessary packages
import streamlit as st

# Page title
st.title("Introduction to Graph Databases")

# Introduction
st.markdown("""
Graph databases are database management systems designed to represent and query complex relationships between data. 
They are particularly useful for use cases such as social networks, recommendations, fraud detection, and more.

In this lab, you will explore graph databases using **Neo4j**, one of the most popular solutions in this field.
""")

# Section: Why use graph databases?
st.header("Why use graph databases?")
st.markdown("""
Graph databases allow you to:
- Model complex relationships intuitively.
- Perform fast queries on deep relationships.
- Solve complex problems like shortest paths, communities, or recommendations.

They use a structure of **nodes** (entities) and **edges** (relationships) to represent data.
""")

# Section: Resources for the lab
st.header("Resources for the Lab")
st.markdown("""
For this lab, you will use **Neo4j** and explore sample datasets. Here are the steps to follow:

1. Visit the following site to access Neo4j's interactive guides:
   - [Neo4j Sample Datasets](https://console-preview.neo4j.io/guides/sample-datasets)

2. Choose one of the available datasets, such as:
   - Social networks.
   - Movie recommendations.
   - Knowledge bases.

3. Follow the instructions to import the data and execute Cypher queries (Neo4j's query language).

4. Try to answer the following questions:
   - What are the nodes and relationships in your dataset?
   - Can you find the most frequent relationships?
   - Can you identify communities or clusters in the data?
""")

# Section: Lab objectives
st.header("Lab Objectives")
st.markdown("""
The objective of this lab is to familiarize yourself with:
- Modeling data as graphs.
- Using Neo4j to import and query data.
- Writing Cypher queries to extract useful information.

By the end of this lab, you should understand how graph databases can be used to solve complex problems.
""")

# Section: Additional resources
st.header("Additional Resources")
st.markdown("""
- [Neo4j Official Documentation](https://neo4j.com/docs/)
- [Cypher Query Language](https://neo4j.com/developer/cypher/)
- [Neo4j Examples and Tutorials](https://neo4j.com/developer/)

Enjoy exploring and have fun with graphs!
""")