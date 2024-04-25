function extractHtmlTags(inputString) {
    const htmlTagsRegex = /<[^>]*>/g; // Regular expression to match HTML tags
    const htmlTagsArray = inputString.match(htmlTagsRegex); // Find all HTML tags in the input string
    
    return htmlTagsArray || []; // Return the array of HTML tags, or an empty array if no tags found
}

export default function htmlCorte(cuttedText,originalText){
    const htmlTagsRegex = /<[^>]*>/g; // Regular expression to match HTML tags
    const cuttedTextTags = extractHtmlTags(cuttedText);
    const originalTextTags = extractHtmlTags(originalText);
    let newText=cuttedText;
    for (let index = cuttedTextTags.length; index >= 0&&index<=originalTextTags.length/2; index--) {
        if((originalTextTags.length-index-1)<cuttedTextTags.length)
        {
            continue
        }
        else{
            newText+=originalTextTags[originalTextTags.length-index-1]
        }
    }   
    return newText;
}

