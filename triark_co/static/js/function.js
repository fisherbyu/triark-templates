function extractTitleAndContent(str, startSubstring, endSubstring) {
    // Extract the title
    const extractContents = function(str, startSubstring, endSubstring) {
      // Find the start index of the start substring
      const startIndex = str.indexOf(startSubstring);
  
      // If the start substring is not found, return an empty string
      if (startIndex === -1) {
        return "";
      }
  
      // Find the end index of the end substring
      const endIndex = str.indexOf(endSubstring, startIndex + startSubstring.length);
  
      // If the end substring is not found, return an empty string
      if (endIndex === -1) {
        return "";
      }
  
      // Return the contents between the start and end substrings
      return str.substring(startIndex + startSubstring.length, endIndex);
    };
  
    // Extract the content
    const extractContentsAfterSubstring = function(str, substring) {
      // Find the index of the substring
      const index = str.indexOf(substring);
  
      // If the substring is not found, return an empty string
      if (index === -1) {
        return "";
      }
  
      // Return the contents after the substring
      return str.substring(index + substring.length);
    };
  
    const title = extractContents(str, startSubstring, endSubstring);
    const content = extractContentsAfterSubstring(str, endSubstring);
  
    // Return the title and content as a string formatted like a Python dictionary
    return `{"title": "${title}", "content": "${content}"}`;
  }
  

// Select all p elements on the page
const pElements = document.querySelectorAll("p");

// Initialize an empty output string
let output = "[";

// Iterate over the p elements
for (let i = 0; i < pElements.length; i++) {
  // Get the inner text of the p element
  const str = pElements[i].innerText;

  // Extract the title and content
  const startSubstring = "<!--";
  const endSubstring = "-->";
  const result = extractTitleAndContent(str, startSubstring, endSubstring);

  // Add the result to the output string
  output += result;

  // Add a comma after the result, except for the last element
  if (i < pElements.length - 1) {
    output += ",";
  }
}

// Close the output string
output += "]";

// Output the output string to the console
console.log(output);
