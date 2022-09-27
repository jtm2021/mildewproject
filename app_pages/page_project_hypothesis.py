import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect affected cherry leaves to have clear marks/signs, "
        f"that are powdery looking patches, that can differentiate from a healthy leaf. \n\n"
        f"* An Image Montage, shows that typically an infected leaf has fungal infection across. "
        f"It is evidenced by an opaqueness characteristic along the venules of the leaves. \n\n"
        f"* Average Image, Variability Image and Difference between Averages studies reveal "
        f"a distinct pattern to differentiate one from another."

    )