
# names=df['name']
# addresses=df['address']
# images=df['image']
# ratings=df['rating']
# reviews=df['reviews']

# thelist = []
# name_tuples = [i for i in names]
# address_tuples = [i for i in addresses]
# image_tuples = [i for i in images]
# rating_tuples = [i for i in ratings]
# review_tuples = [i for i in reviews]

# print(name_tuples)
# thelist.append(name_tuples)
# print(thelist)


# address_tuples = []
# for a,b,c,d,e in zip(names, addresses, images, ratings, reviews):
# 	cursor.execute('''
# 		INSERT INTO 
# 		facilities (name, address, images, rating, reviews) 
# 		VALUES
# 		(%(a)s,%(b)s,%(c)s,%(d)s,%(e)s);
# 	''', {"a":a,"b":b,"c":c,"d":d,"e":e})


# cursor.executemany('''
# 		INSERT INTO 
# 		facilities (name, address, image, rating, reviews) 
# 		VALUES
# 		(%s,%s,%s,%s,%s);
# 	''', 
# 	(
# 		(
# 			name, 
# 			address, 
# 			('' if np.nan is image else image), 
# 			(0 if np.nan is rating else float(rating)), 
# 			(0 if np.nan is reviews else float(reviews))
# 		) 
# 		for 
# 			name, address, image, rating, reviews
# 		in 
# 			zip(names, addresses, images, ratings, reviews)
# 	)
# )