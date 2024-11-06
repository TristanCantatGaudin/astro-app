import streamlit as st
import numpy as np




st.markdown("""
<style>
[data-baseweb="base-input"]{
background:#ffdddd;
}

input[class]{
font-weight: regular;
font-size:120%;
color: black;
}
</style>
""", unsafe_allow_html=True)



def update_valDistMod():
	newPc = float(st.session_state.valPc)
	newDm = 5*np.log10(newPc)-5
	st.session_state.valDistMod = f"{newDm:.2f}"

def update_valPc():
    newDm = float( st.session_state.valDistMod )
    newPc = 10**(1+(newDm/5.))
    st.session_state.valPc = f"{newPc:e}"   

col1,col2,col3 = st.columns(3)
valPc = col1.text_input('distance in parsecs:', 
						value = 400, 
						key = 'valPc', 
						on_change = update_valDistMod)


valDistMod = col2.text_input('distance modulus:', 
                        value = 8, 
                        key = 'valDistMod', 
                        on_change= update_valPc)
                        

magWD = 12 + float(st.session_state.valDistMod)
magSun = 4.83 + float(st.session_state.valDistMod)
magRC = 0.5 + float(st.session_state.valDistMod)
absMag21 = 21 - float(st.session_state.valDistMod)
st.session_state.text = f"""At that distance: 
* a white dwarf has magnitude    **{magWD:.2f}**
* the Sun has magnitude          **{magSun:.2f}**
* a red clump star has magnitude **{magRC:.2f}**
* an apparent magnitude of 21 is an absolute magnitude of **{absMag21:.2f}** """

# Display the modified text
st.markdown(st.session_state.text)    
#st.session_state
                        
# - - - - 


st.write('## Parsecs to distance modulus')
#
st.write(r'$(m-M)_0 = 5 \times \log_{10} d_{\mathrm{pc}} - 5$')
st.code(r'distanceModulus = 5*np.log10(distancePc)-5 ')
#
st.write(r'$d_{\mathrm{pc}} = 10^{ 1 + \frac{(m-M)_0}{5} }$')
st.code(r'distancePc = 10**(1+(distanceModulus/5.)) ')


st.write('## Parsecs to parallax')
st.code(r'distancePc = 1./parallaxArcsec = 1000./parallaxMas ')


st.write('## Parallax to distance modulus')
st.write(r'$(m-M)_0 = 10 - 5 \times \log_{10} \varpi$')
st.write(r'$\varpi = 10 ^ \frac{10 - (m-M)_0}{5}$')

st.write('## Absolute magnitude')
st.write('uncorrected for interstellar extinction')
st.code(r'Gabs = G + 5*(np.log10(parallax/1000.)+1) ')
st.write('(with parallax in mas)')




