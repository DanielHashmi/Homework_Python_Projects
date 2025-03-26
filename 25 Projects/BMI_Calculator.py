import streamlit as st

def calculate_bmi(height_feet, height_inches, weight_kg):
  total_inches = (height_feet * 12) + height_inches
  height_meters = total_inches * 0.0254
  bmi = weight_kg / (height_meters ** 2)
  return bmi

def main():
  st.title("BMI Calculator")
  st.header("Enter your details:")
  height_feet = st.number_input("Height (feet)", min_value=0, max_value=10, value=5, step=1)
  height_inches = st.number_input("Height (inches)", min_value=0, max_value=11, value=6, step=1)
  weight_kg = st.number_input("Weight (kg)", min_value=0, max_value=500, value=70, step=1)


  if st.button("Calculate BMI"):
    bmi = calculate_bmi(height_feet, height_inches, weight_kg)
    st.write("Your BMI is:", round(bmi, 2))
    if bmi < 18.5:
      st.write("You are underweight.")
    elif bmi < 25:
      st.write("You are normal and have a healthy weight.")
    elif bmi < 30:
      st.write("You are overweight.")
    else:
      st.write("You are in the obesity range.")

if __name__ == "__main__":
  main()
