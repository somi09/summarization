from src.model import model, tokenizer


def summarize(text, maxSummarylength=500):
    # Encode the text and summarize
    chunks = split_text_into_pieces(text)
    print(len(chunks))
    summaries = []
    for chunk in chunks:
        tokens = tokenizer(chunk, truncation=True, padding="longest", return_tensors="pt")
        summary = model.generate(**tokens)
        summaries.append(tokenizer.decode(summary[0]))
    draft = " ".join(summaries)
    # tokens = tokenizer(draft, truncation=True, padding="longest", return_tensors="pt")
    # summary = model.generate(**tokens)
    return draft

def split_text_into_pieces(text,
                           max_chunk=500):
    text = text.replace('.', '.<eos>')
    text = text.replace('?', '?<eos>')
    text = text.replace('!', '!<eos>')
    sentences = text.split('<eos>')

    current_chunk = 0 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    return chunks


'''testing'''

# text = '''
# Will The Game Stop with Gamestop Or Is This Just The Beginning? Crypto, Markets, Trading The GameStop squeeze on short-sellers is an extraordinary event in markets, where at face value, retail traders and investors have worked together in an attempt to put some of the largest wall street institutions out of business. The events can be interpreted with many viable lenses and there are ironies baked in that are pure serendipity. There has been a centrally controlled game in the global financial system in which insiders benefited while outsiders got hurt that comes to a head with a company called GameStop. The broking firm of most of the retail side of this warfare ‘RobinHood’ is literally stealing from its poor, retail investors to give to its rich, capital backers. One of the historical realities of this game has been that macro-investing – the sages of not only portfolio management, but often also sophisticated social and cultural figures – have had a hard time making money in markets now for decades. With government policy dictating markets in greater degrees since the mid-90’s, the politically connected have been more likely to survive while the sophisticated and capable have been more likely to struggle. Quantitative and high-frequency trading has entered and changed the structure of global markets with this change invited through central banking policy characterised by moral hazard. Commerce and politics has grown closer and so commercial survival has demanded a political edge. Although what I really want to talk about is how market structure has changed since 1995 and how this has contributed to the situation here, a little bit of the history is first required. Drinks on Alan The tequila crises was one of the first events in late 1994, early 1995 in which insiders were bailed out and the might of the U.S. governments political capital was used to organise $50-$80 billion USD in capital for political insiders capital at risk in Mexico.  The big moral hazard there was ex-Goldman Sachs Treasury Secretary Robert Rubin using the state ‘Exchange Stabilisation Fund’ to support a Mexican bailout that protected Goldman Sachs investments. It was Alan Greenspan presiding over the Federal Reserve at the time, meeting with the men in power with sharp suits and important titles. It probably even felt like the right thing to do. This ‘Greenspan put’ as his actions became known in the investing world, fundamentally changed the structure of markets and gave enormous knowledge and power to the politically connected.  (This concept, of a ‘Greenspan put’ refers to the willingness of the Federal Reserve chairman to protect asset prices. A put is insurance against declining asset prices in which the put seller can lose big.) Meet Victor Niederhoffer. Victor Niederhoffer is one of the most successful people alive today.  Niederhoffer studied statistics and economics at Harvard and the University of Chicago, was a finance professor at the University of California and while at college he co-founded an investment bank. Having never picked up a racquet before Harvard, Niederhoffer won the squash national junior title a year later, graduated as the national intercollegiate champion, won the U.S. nationals 5 times and defeated one of the greatest players in the history of the sport in the North American Open, becoming a member of the squash hall of fame. His investment record is tremendous, with an average of a 35% return annualised and once working for fellow legend of funds management George Soros. When it came time for his son to learn the family business, Soros sent his son to Niederhoffer. Niederhoffers books ‘Practical Speculation’ and ‘The Education of a Speculator’ are essential reading for market speculation, a ‘Reminiscences of a Stock Operator’ for the thinking man.  And with changes in how the global financial system became more political, men like Niederhoffer just don’t seem to be around anymore. Maybe they don’t exist anywhere in this limited, unnatural and politically charged environment. Because Victor Niederhoffer, one of the singularly most impressive people you may find, blew his hedge fund up in 1997 in a highly statistically improbable event, in which he sold puts that were targeted by market mechanics, rather than ‘truth’.  A new layer had been added to the Keynesian beauty contest that is global markets, in which leveraged speculators could now make the market so volatile that the entire equity market could change trajectory over a period of months to target rational, risky and forward thinking positions. Normally the type of technical work that the market completed when Niederhoffer sold his puts would prove the future direction of the market so that a speculator could reasonably presume that they were taking a strong risk-adjusted position. The trade setup that emerged in this new type of market - which I call ‘the second bite of the apple’ -is a disadvantage to people who understand markets and understand risk. It takes a professional back to school and adds a new technical layer to fundamental analysis. The market here is more leveraged, more volatile, more aggressive, better for types of trading and worse for investing. The fundamentals no longer matter; and this was demonstrated only 5 years later with what could be the largest bubble of viable assets in history was formed – the NASDAQ bubble in which household blue chip stocks today lost 98% of their value. This was new. It destroyed Niederhoffer, who was quoted by the Washington Post on the day   ‘ “I’ve made that trade hundreds of times in the past 15 years” he whispered “I believe it’s a good trade. It was a one in 2,000 shot that the market would decline like that” ‘ And it baffled many sophisticated market participants for a long time afterwards. But we can actually see a change in the market! When we consider the S&P500 before and after this event (compare A with B), we can see a fundamental change in the market structure, especially in volatility, and how aggressively the market would trade (look at the second squeeze that would almost put his positions offside a second time – if he had them!). Greenspans moral hazard of late 1994/1995 fundamentally changed the market in a new way. Extraordinary people who were never wrong in risk-adjusted terms and who understood markets were carried out of them horizontally by players with leverage, who knew your position, who were more predatory in nature, had no idea about which direction the market headed in, did not care which direction the market ultimately headed in and the people who actually understood and cared about the big picture were now, irrelevant. They would leverage a short position to 500% of the total market capitalisation of the company they were selling simply to crush it into oblivion, and were able to because of a new reality in the global financial system and a new structure in markets. Financial markets were now more poker – positioning, position size and leverage – and less fundamental – for example, what are the future cash-flows of this business? Does this matter? There is a slice of the population, and not a small slice, who would blindly exchange a Niederhoffer for the more savage trader who profited from his demise any day of the week.  Both are rich, successful and perceptibly in the same dirty business, and for a lot of people they might be thrown into the same basket. Why do they care if a hedge fund manager blows up? Well, because we submit that a new epoch of financial markets had begun. We now had a post-modernist, post-truth financial system headed by a mob characterised by a view of their own power and control in which they could manifest truth and reality as they saw fit – but mostly for their mates on the inside. Of course this was fine for the people creating the financial system, because rationalising your own status, your own righteousness in the use of power and your ability to make earth-changing decisions for the benefits of your powerful friends would feel as if things were the way they should be. Why would they care about some hedge-fund managers positions? He knows the game he was getting himself into and should be a generally astute individual, expert in perceiving and managing risk. But this new financial elite establishment DID care about hedge-fund managers losses, just that it was only specific hedge-fund managers that they cared about. In 1998, Long Term Capital Management (LTCM) busted during the 1998 Russian financial crises, losing up to $4.6 billion USD in face value of an approximately $1 billion USD fund. LTCM was founded by a former vice-chairman of Salomon Brothers (of legendary fame in bonds) and their board included Myron S. Scholes and Robert C. Merton of Black-Scholes fame, who won the Nobel Memorial Prize in Economic Sciences in 1997 for their revolutionary equation in options pricing. Their strategy was extremely highly leveraged (debt to equity over 25:1) trading to lock markets up with theoretical modelling overlays onto the real-world market reality.   At face-value LTCM relied on expertise, but in practice it relied on size and reputation of the people involved, evidenced by its catastrophic failure. To cut a long story short, Alan Greenspans Federal Reserve brokered a deal to rescue LTCM with the benefactor of that deal being Goldman Sachs, who had access to the assets sold at firesale – again a benefactor of the interventions of public institutions filled with their own alumni. The Federal Reserve provided $3.6 billion USD of recapitalisation. For Victor Niederhoffer there is some circular logic that emerges here, that spites and gaslights. LTCM was a group of insiders using incredible amounts of leverage to make wrong decisions in markets. Their existence is precipitated in the dangerous new world of Greenspans Federal Reserve, yet a world in which they ultimately fail on paper, are bailed out in practice.   It spites Niederhoffer because the impact on the market as a result of their failure is the best piece of evidence that Victor Niederhoffer was ultimately wrong when the positions that he took that ended his career would have been threatened again in 1998 in this asset price collapse (his positions were challenged again in 1998, validating the argument that the aggressive, leveraged, even vicious targeting of his positions was natural after all).  But this irresponsible group, who were wrong, and who would go on to invalidate Niederhoffer, who would have been right before this fundamental change in reality and market structure, were then bailed-out, while he began rebuilding his career brick by brick. With these two famous moral hazards – of the Tequila Crises and LTCM bailout, the qualitative features of global financial markets fundamentally change. The big-picture thinkers who understand macro-level knowledge in a unique and sophisticated form give way to aggressive, predatory, leveraged, profit taking machinery.  The result had been written in, in 1995. 1995-2008 was one epoch As time went on, events in 1995 and 1998 became the Nasdaq bubble, the Federal Reserve policy response to the Nasdaq bubble became the housing bubble that led into the global financial crisis. The Global Financial Crisis of 2008 was a result of Greenspans put money and the financial institutions writing the rules for financial institutions. Bear Sterns was allowed to fail and Goldman Sachs got bailout money. Macro-investors like Niederhoffer were never less successful around this time onward, and Victor Niederhoffer blew his fund up a second time during this period. Market speculation was now more purely a highly leveraged, volatile and aggressive game in which fundamentals essentially did not matter. The politically connected were able to exploit event risk, with insider knowledge providing superior returns. The Federal Reserve now provided returns. 2008-2020 was another epoch After 25 years of this phenomenon creeping into global markets, in 2020, the public were ahead of it for the first time. During the coronavirus collapse, aggressive retail investors bought, perhaps for the
# '''
# print(summarize(text))