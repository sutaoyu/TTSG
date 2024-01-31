from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from scipy.spatial.distance import euclidean, num_obs_dm
import numpy as np
from sklearn.cluster import KMeans

# bigram
segment_bigram = lambda text: " ".join([word + text[idx + 1] for idx, word in enumerate(text) if idx < len(text) - 1])
 

#load dataset
texts = []

with open("20news_brio_summary.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.replace('-',"")
        texts.append(line.strip())


vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(texts))
 
word = vectorizer.get_feature_names_out()
print("word feature length: {}".format(len(word)))
 
tfidf_weight = tfidf.toarray()


#clustering 
kmeans = KMeans(n_clusters=20)
kmeans.fit(tfidf_weight)
 
print(kmeans.cluster_centers_)
sumlabel = []
for index, label in enumerate(kmeans.labels_, 1):
    #print("index: {}, label: {}".format(index, label))
    sumlabel.append(label)
 
print("inertia: {}".format(kmeans.inertia_)) 


#generate topic documents
textnum = 5
newtxt = []
for iclust in range(kmeans.n_clusters):
    cluster_pts = tfidf_weight[kmeans.labels_ == iclust]
    cluster_pts_indices = np.where(kmeans.labels_ == iclust)[0]

    cluster_cen = kmeans.cluster_centers_[iclust]
    distance = [euclidean(tfidf_weight[idx], cluster_cen) for idx in cluster_pts_indices]
    print('distance:', distance)
    
    closest_pt_idx = []
    num = len(distance)
    if num <= textnum:
        n = num-1
        _num_sort = np.argpartition(distance, num)[:n]

        print('------', num)
        print('closest n point to cluster center: ', cluster_pts[_num_sort])
        print('closest n index of point to cluster center: ', cluster_pts_indices[_num_sort])
        closest_pt_idx = cluster_pts_indices[_num_sort]

        summ = []
        for i in range(num):  
            print(closest_pt_idx[i])
            print(corpus[closest_pt_idx[i]])
            summ.append(corpus[closest_pt_idx[i]])
    else:
        _textnum_sort = np.argpartition(distance, textnum)[:textnum]

        print('------')
        print('closest textnum point to cluster center: ', cluster_pts[_textnum_sort])
        print('closest textnum index of point to cluster center: ', cluster_pts_indices[_textnum_sort])
        print('------')
        closest_pt_idx = cluster_pts_indices[_textnum_sort]

        summ = []
        for i in range(textnum):  
            print(closest_pt_idx[i])

            print(corpus[closest_pt_idx[i]])
            summ.append(corpus[closest_pt_idx[i]])
            
    
    new =  "|||||".join(summ)
    newtxt.append(new)
    print(new)


#save files
def text_save(file_name, datas):
    file = open(file_name,'w')
    print(len(datas))
    print('----')
    print(datas[0])
    for i in range(len(datas)):
        s = str(datas[i]).replace('[]','').replace(']','') 
        s = s.replace('–','') +'\n' 
        file.write(s)
    file.close()
    print('Successfully saved!')

text_save("20news_newtxt", newtxt)

import csv
with open('20news_newtxt', 'r') as input_file:
	with open('20news_newtxt.csv', 'w', newline='') as output_file:
		writer = csv.writer(output_file)
		header_row = ['text']
        writer.writerow(header_row)
        for line in input_file:
			row = line.strip().split('\t')
			writer.writerow(row)
