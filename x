digraph Tree {
node [shape=box, fontname="helvetica"] ;
edge [fontname="helvetica"] ;
0 [label="x[0] <= 0.5\ngini = 0.5\nsamples = 6\nvalue = [3, 3]"] ;
1 [label="gini = 0.0\nsamples = 1\nvalue = [0, 1]"] ;
0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
2 [label="x[0] <= 1.5\ngini = 0.48\nsamples = 5\nvalue = [3, 2]"] ;
0 -> 2 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
3 [label="gini = 0.0\nsamples = 1\nvalue = [1, 0]"] ;
2 -> 3 ;
4 [label="x[0] <= 2.5\ngini = 0.5\nsamples = 4\nvalue = [2, 2]"] ;
2 -> 4 ;
5 [label="gini = 0.0\nsamples = 1\nvalue = [0, 1]"] ;
4 -> 5 ;
6 [label="x[0] <= 3.5\ngini = 0.444\nsamples = 3\nvalue = [2, 1]"] ;
4 -> 6 ;
7 [label="gini = 0.0\nsamples = 1\nvalue = [1, 0]"] ;
6 -> 7 ;
8 [label="x[0] <= 4.5\ngini = 0.5\nsamples = 2\nvalue = [1, 1]"] ;
6 -> 8 ;
9 [label="gini = 0.0\nsamples = 1\nvalue = [0, 1]"] ;
8 -> 9 ;
10 [label="gini = 0.0\nsamples = 1\nvalue = [1, 0]"] ;
8 -> 10 ;
}
