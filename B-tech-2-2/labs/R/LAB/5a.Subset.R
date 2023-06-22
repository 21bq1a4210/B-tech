data(iris)
#subset of dataset using subset()
subset_versicolor<-subset(iris, Species == 'versicolor')
print(subset_versicolor)
'output:
    Sepal.Length Sepal.Width Petal.Length
51           7.0         3.2          4.7
52           6.4         3.2          4.5
53           6.9         3.1          4.9
54           5.5         2.3          4.0
55           6.5         2.8          4.6
56           5.7         2.8          4.5
57           6.3         3.3          4.7
58           4.9         2.4          3.3
59           6.6         2.9          4.6
60           5.2         2.7          3.9
61           5.0         2.0          3.5
62           5.9         3.0          4.2
63           6.0         2.2          4.0
64           6.1         2.9          4.7
65           5.6         2.9          3.6
66           6.7         3.1          4.4
67           5.6         3.0          4.5
68           5.8         2.7          4.1
69           6.2         2.2          4.5
70           5.6         2.5          3.9
71           5.9         3.2          4.8
72           6.1         2.8          4.0
73           6.3         2.5          4.9
74           6.1         2.8          4.7
75           6.4         2.9          4.3
76           6.6         3.0          4.4
77           6.8         2.8          4.8
78           6.7         3.0          5.0
79           6.0         2.9          4.5
80           5.7         2.6          3.5
81           5.5         2.4          3.8
82           5.5         2.4          3.7
83           5.8         2.7          3.9
84           6.0         2.7          5.1
85           5.4         3.0          4.5
86           6.0         3.4          4.5
87           6.7         3.1          4.7
88           6.3         2.3          4.4
89           5.6         3.0          4.1
90           5.5         2.5          4.0
91           5.5         2.6          4.4
92           6.1         3.0          4.6
93           5.8         2.6          4.0
94           5.0         2.3          3.3
95           5.6         2.7          4.2
96           5.7         3.0          4.2
97           5.7         2.9          4.2
98           6.2         2.9          4.3
99           5.1         2.5          3.0
100          5.7         2.8          4.1
    Petal.Width    Species
51          1.4 versicolor
52          1.5 versicolor
53          1.5 versicolor
54          1.3 versicolor
55          1.5 versicolor
56          1.3 versicolor
57          1.6 versicolor
58          1.0 versicolor
59          1.3 versicolor
60          1.4 versicolor
61          1.0 versicolor
62          1.5 versicolor
63          1.0 versicolor
64          1.4 versicolor
65          1.3 versicolor
66          1.4 versicolor
67          1.5 versicolor
68          1.0 versicolor
69          1.5 versicolor
70          1.1 versicolor
71          1.8 versicolor
72          1.3 versicolor
73          1.5 versicolor
74          1.2 versicolor
75          1.3 versicolor
76          1.4 versicolor
77          1.4 versicolor
78          1.7 versicolor
79          1.5 versicolor
80          1.0 versicolor
81          1.1 versicolor
82          1.0 versicolor
83          1.2 versicolor
84          1.6 versicolor
85          1.5 versicolor
86          1.6 versicolor
87          1.5 versicolor
88          1.3 versicolor
89          1.3 versicolor
90          1.3 versicolor
91          1.2 versicolor
92          1.4 versicolor
93          1.2 versicolor
94          1.0 versicolor
95          1.3 versicolor
96          1.2 versicolor
97          1.3 versicolor
98          1.3 versicolor
99          1.1 versicolor
100         1.3 versicolor
'

subset_petel_length_gt4<-sbuset(iris,Petal.Length>4)
print(subset_versicolor)
'output:
    Sepal.Length Sepal.Width Petal.Length
51           7.0         3.2          4.7
52           6.4         3.2          4.5
53           6.9         3.1          4.9
54           5.5         2.3          4.0
55           6.5         2.8          4.6
56           5.7         2.8          4.5
57           6.3         3.3          4.7
58           4.9         2.4          3.3
59           6.6         2.9          4.6
60           5.2         2.7          3.9
61           5.0         2.0          3.5
62           5.9         3.0          4.2
63           6.0         2.2          4.0
64           6.1         2.9          4.7
65           5.6         2.9          3.6
66           6.7         3.1          4.4
67           5.6         3.0          4.5
68           5.8         2.7          4.1
69           6.2         2.2          4.5
70           5.6         2.5          3.9
71           5.9         3.2          4.8
72           6.1         2.8          4.0
73           6.3         2.5          4.9
74           6.1         2.8          4.7
75           6.4         2.9          4.3
76           6.6         3.0          4.4
77           6.8         2.8          4.8
78           6.7         3.0          5.0
79           6.0         2.9          4.5
80           5.7         2.6          3.5
81           5.5         2.4          3.8
82           5.5         2.4          3.7
83           5.8         2.7          3.9
84           6.0         2.7          5.1
85           5.4         3.0          4.5
86           6.0         3.4          4.5
87           6.7         3.1          4.7
88           6.3         2.3          4.4
89           5.6         3.0          4.1
90           5.5         2.5          4.0
91           5.5         2.6          4.4
92           6.1         3.0          4.6
93           5.8         2.6          4.0
94           5.0         2.3          3.3
95           5.6         2.7          4.2
96           5.7         3.0          4.2
97           5.7         2.9          4.2
98           6.2         2.9          4.3
99           5.1         2.5          3.0
100          5.7         2.8          4.1
    Petal.Width    Species
51          1.4 versicolor
52          1.5 versicolor
53          1.5 versicolor
54          1.3 versicolor
55          1.5 versicolor
56          1.3 versicolor
57          1.6 versicolor
58          1.0 versicolor
59          1.3 versicolor
60          1.4 versicolor
61          1.0 versicolor
62          1.5 versicolor
63          1.0 versicolor
64          1.4 versicolor
65          1.3 versicolor
66          1.4 versicolor
67          1.5 versicolor
68          1.0 versicolor
69          1.5 versicolor
70          1.1 versicolor
71          1.8 versicolor
72          1.3 versicolor
73          1.5 versicolor
74          1.2 versicolor
75          1.3 versicolor
76          1.4 versicolor
77          1.4 versicolor
78          1.7 versicolor
79          1.5 versicolor
80          1.0 versicolor
81          1.1 versicolor
82          1.0 versicolor
83          1.2 versicolor
84          1.6 versicolor
85          1.5 versicolor
86          1.6 versicolor
87          1.5 versicolor
88          1.3 versicolor
89          1.3 versicolor
90          1.3 versicolor
91          1.2 versicolor
92          1.4 versicolor
93          1.2 versicolor
94          1.0 versicolor
95          1.3 versicolor
96          1.2 versicolor
97          1.3 versicolor
98          1.3 versicolor
99          1.1 versicolor
100         1.3 versicolor
'

aggregate_mean_sepal_length <- aggregate(Sepal.Length ~ Species, data = iris, FUN = mean)
print(aggregate_mean_sepal_length)
'ottput:
Species Sepal.Length
1     setosa        5.006
2 versicolor        5.936
3  virginica        6.588
'
aggregate_max_petal_width <- aggregate(Petal.Width ~ Species, data = iris, FUN = max)
print(aggregate_max_petal_width)
'output:
Species Sepal.Length
1     setosa        5.006
2 versicolor        5.936
3  virginica        6.588
'