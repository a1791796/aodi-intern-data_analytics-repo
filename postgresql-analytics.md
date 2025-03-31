
What makes PostgreSQL a good choice for data analytics?

PostgreSQL provides built-in analytics tools, for example
Window Functions:Allow calculations without output one add-up result
Indexing for Faster Queries: create index before select the data for faster retreive data.
JSON and JSONB Support: support for unstructured data.

How do JOIN operations help in analyzing relational data?

JOIN operations are crucial when analyzing relational data because they allow you to combine data from different tables based on common keys or relationships,
this can reduce a lot of workload.

What are window functions, and how can they be used for user trend analysis?

Window functions is to calculate the row, one kind of aggregrate function but it's more powerful because it preserve the row's individuality in the result set,
the common aggregrate function we use usually return only two rows, which are name and aggregrated value(sum or mean). Analytics may need more information rather than just simply add up.

Why is query optimization important, and how does EXPLAIN ANALYZE help?

 query optimization is important because it can improve the performance and efficiency of database.
 EXPLAIN ANALYZE provides detailed insights into how the database engine executes a query, it helps analytics to know where takes the longest time and where they can improve.
