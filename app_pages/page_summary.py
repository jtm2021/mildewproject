import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects a wide range of plants. "
        f"They are caused by many different species of fungi in the order Erysiphales.\n"
        f"* Powdery mildew is one of the easier plant diseases to identify, as its "
        f"symptoms are quite distinctive.\n"
        f"* Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, "
        f"an obligate biotrophic fungus. "
        f"Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, "
        f"rendering them unmarketable due to the covering of white fungal growth on the cherry surface.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 images that are either "
        f"healthy or affected with powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/jtm2021/mildewproject/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a "
        f"cherry leaf that is healthy and that contains powdery mildew.\n"
        f"* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew. "
        )