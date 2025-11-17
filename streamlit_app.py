import streamlit as st
import clipspy
import logging 

# Setup working environment
logging.basicConfig(level=15, format='%(message)s')

env = clipspy.Environemnt()
router = clipspy.LoggingRouter()
env.add_router(router)


# Input

name = st.text_input("Enter your name")

# Knowledge base
env.build('(deftemplate result (slot name))')

env.assert_string(f'(result (name "{name}"))')

# inference
env.run()


# output
results = []
for fact in env.facts():
    if fact.template.name == 'result':
        results.append(fact['name'])

st.write(results[0], "output")