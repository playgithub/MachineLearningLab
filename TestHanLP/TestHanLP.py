import hanlp
import jieba
import jieba.posseg as pseg
import jieba.analyse

sentence = '质量不大好'


# 分词
tokenizer = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')

print('-'*6, 'hanlp', '-'*6)

result = tokenizer(sentence)
print(' '.join(result))

print('-'*6, 'jieba', '-'*6)

result = jieba.cut(sentence)
print(' '.join(list(result)))


#words = pseg.cut("sentence")
#for word, flag in words:
#   print('%s %s' % (word, flag))

print('-'*6, 'jieba analyse', '-'*6)

for x, w in jieba.analyse.extract_tags(sentence, withWeight=True):
    print('%s %s' % (x, w))
print('-'*40)
print('TextRank')
print('-'*40)
for x, w in jieba.analyse.textrank(sentence, withWeight=True):
    print('%s %s' % (x, w))