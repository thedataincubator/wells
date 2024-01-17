import streamlit as st

from database import query_db
from plotting import plot_wells

def app():
    st.title('Wells in the US')
    st.markdown('Select the minimum depth and gradient to display:')
    
    min_depth = st.number_input('Min depth', 0, 10000, step=500, value=5000)
    min_gradient = st.number_input('Min gradient', 0., 0.1, step=0.005, value=0.01, format='%0.3f')
    
    data = query_db(min_depth, min_gradient)
    st.write(plot_wells(data))
    
if __name__ == '__main__':
    app()
