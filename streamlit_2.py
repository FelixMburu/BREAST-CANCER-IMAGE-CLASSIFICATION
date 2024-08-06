# -*- coding: utf-8 -*-
"""Streamlit 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SXeNaye9aj71neB3eJIHKeCwySXIKogZ
"""

#Streamlit deployment
st.title('Model Deployment with Streamlit')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    image = transform(image)
    image = image.unsqueeze(0)  # Add batch dimension
    output = model(image)
    _, predicted = torch.max(output, 1)
    st.write(f'Predicted class: {predicted.item()}')