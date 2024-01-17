import streamlit as st

from database import query_db
from plotting import plot_wells

def app():
    st.title('Wells in the US')
    
    data = query_db(5000, 0.01)
    st.write(plot_wells(data))
    
    
if __name__ == '__main__':
    app()
