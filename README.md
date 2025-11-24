# Temperature Conversion Tool - Python Project

1.Project Description

This Python project is a Temperature Conversion Tool that enables users
to convert temperature values between Celsius, Fahrenheit, and Kelvin
scales. It provides a simple, interactive console interface for accurate
temperature conversion, demonstrating core programming concepts such as
functions, conditional statements, and user input handling.

2.Features:

\- Convert temperatures between Celsius, Fahrenheit, and Kelvin -
Interactive command-line interface with clear user prompts - Handles
invalid input gracefully with appropriate messages

\- Modular design using functions or classes for conversion logic - Easy
extensibility for additional temperature scales

3.How It Works

The tool prompts the user to enter the temperature value, the input
scale (c, f, or k), and the output scale (c, f, or k). According to
these inputs, the program performs the appropriate conversion using
standard temperature conversion formulas:

\- Celsius to Fahrenheit: (c×9\5)+32 
\- Fahrenheit to Celsius:(f−32)×5\9 
\- Celsius to Kelvin: c+273.15

\- Kelvin to Celsius: k−273.15

\- Fahrenheit to Kelvin and Kelvin to Fahrenheit conversions are
calculated via intermediate Celsius conversions.

4.Requirements

\- Python 3.x installed on your system

5.How to Run

- Run the Python script:
      text 
      python temperature_conversion_tool.py

\- Follow on-screen prompts to enter: 
\- Temperature value (numeric)

\- Input temperature scale (c,f, or k)

\- Desired output temperature scale (c, f, or k) - View the converted
temperature result.

\- Optionally repeat or exit the program.

6.Future Enhancements

\- Add a graphical user interface using Tkinter or similar frameworks

\- Include more temperature scales such as Rankine and Réaumur

\- Add conversion history with save/load features

\- Deploy as a web app for online temperature conversion
