from snownlp import SnowNLP
from snownlp import sentiment

sentences = u'质量不大好'

result = SnowNLP(sentences)
print(result.words);

print(result.sentiments)
