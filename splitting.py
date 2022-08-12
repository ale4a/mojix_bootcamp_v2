import streamlit as st

def splitting():
  st.write("""
  ## 2. If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!
  """)

  st.write("""
  ### Example
  """)

  code = '''
  string = “hello world”
  string.split()
  '''

  st.code(code, language='python')

  st.write("""
  ### Output
  """)

  code = '''
  [‘hello’, ‘world’]
  '''
  st.code(code, language='python')
