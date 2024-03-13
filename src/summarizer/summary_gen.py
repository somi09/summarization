from src.model import model, tokenizer


def summarize(text, maxSummarylength=500):
    # Encode the text and summarize
    inputs = tokenizer.encode("summarize: " +
                              text,
                              return_tensors="pt",
                              max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=maxSummarylength,
                                 min_length=int(maxSummarylength/5),
                                 length_penalty=10.0,
                                 num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def split_text_into_pieces(text,
                           max_tokens=900,
                           overlapPercent=10):
    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    print(tokens)

    # Calculate the overlap in tokens
    overlap_tokens = int(max_tokens * overlapPercent / 100)

    # Split the tokens into chunks of size
    # max_tokens with overlap
    pieces = [tokens[i:i + max_tokens]
              for i in range(0, len(tokens),
                             max_tokens - overlap_tokens)]

    #print(len(pieces))

    # Convert the token pieces back into text
    text_pieces = [tokenizer.decode(
        tokenizer.convert_tokens_to_ids(piece),
        skip_special_tokens=True) for piece in pieces]

    return text_pieces

def recursive_summarize(text, max_length=200, recursionLevel=0):
    recursionLevel=recursionLevel+1
    print("######### Recursion level: ",
          recursionLevel,"\n\n######### ")
    tokens = tokenizer.tokenize(text)
    expectedCountOfChunks = len(tokens)/max_length
    max_length=int(len(tokens)/expectedCountOfChunks)+2

    # Break the text into pieces of max_length
    pieces = split_text_into_pieces(text, max_tokens=max_length)

    print("Number of chunks: ", len(pieces))
    # Summarize each piece
    summaries=[]
    k=0
    for k in range(0, len(pieces)):
        piece=pieces[k]
        summary =summarize(piece, maxSummarylength=max_length/3*2)
        summaries.append(summary)

    concatenated_summary = ' '.join(summaries)

    tokens = tokenizer.tokenize(concatenated_summary)

    if len(tokens) > max_length:
        # If the concatenated_summary is too long, repeat the process
        return recursive_summarize(concatenated_summary,
                                   max_length=max_length,
                                   recursionLevel=recursionLevel)
    else:
      # Concatenate the summaries and summarize again
        final_summary=concatenated_summary
        if len(pieces)>1:
            final_summary = summarize(concatenated_summary,
                                  maxSummarylength=max_length)
        return final_summary