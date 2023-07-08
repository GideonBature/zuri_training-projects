// Program for a Simple Calculator

// Take the two numbers and operation

// Using parseFloat to convert the numbers entered as strings into a number

const num1 = parseFloat(prompt("Please Enter First Number"));

const operation = prompt("Please Enter +, -, * or /");

const num2 = parseFloat(prompt("Please Enter Second Number"));

// Use conditional if, else if and else

if (operation == "+") {
  result = num1 + num2;
} else if (operation == "-") {
  result = num1 - num2;
} else if (operation == "*") {
  result = num1 * num2;
} else {
  result = num1 / num2;
}

// Display the Result

alert(`${num1} ${operation} ${num2} = ${result}`);
