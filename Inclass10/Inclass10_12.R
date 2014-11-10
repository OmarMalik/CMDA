################
# INCLASS 10_1 #
################

data(iris)

names(iris)

head(iris)

summary(iris)

a = iris[,1:4]

a_scaled = scale(a)

summary(a_scaled)

distance = dist(a_scaled, method="euclidean")

hier_cl = hclust(distance, method="ward.D")

plot(hier_cl, labels=iris$Species)

rect.hclust(hier_cl, k=3)

groups = cutree(hier_cl, k=3)

print(groups)

# group 1 is seperated into all setosa species with no overlap
# group 2 is seperated into all viginica species with no overlap
# group 3 is mostly in the versicolor species but there are also some virginica and setosa species

################
# INCLASS 10_2 #
################

clusters = kmeans(distance, 3, nstart=100, iter.max=100)

print(clusters)
print(clusters$cluster)
print(clusters$centers)
print(clusters$withinss)
print(clusters$tot.withinss)
print(clusters$betweenss)
print(clusters$size)

cluster_comparison = cbind(groups, clusters$cluster)
cluster_comparison = as.data.frame(cluster_comparison)
names(cluster_comparison) = c("Hierarchical", "kmeans")
cluster_comparison = cbind(iris$Species, cluster_comparison)
print(cluster_comparison)