学习笔记

主要练习了BFS和DFS

BFS 简单易理解， 重点是代码技巧 用一个 队列，神来之笔。

只要理解了这个 队列 对BFS的意义，BFS就比较简单。

上模板：

    def BFS(graph, start, end):
        visited = set()
            queue = [] 
	    queue.append([start]) 
	    while queue: 
		    node = queue.pop() 
		    visited.add(node)
		    process(node) 
		    nodes = generate_related_nodes(node) 
		    queue.push(nodes)
	    # other processing work 

DFS 思想理解起来容易，但实际操作起来 还是难理解，虽然也有模板，但是小变化处理起来还是费解。
比较难搞， 只能多练习。

    def dfs(node, visited):
        if node in visited: # terminator
    	    # already visited 
    	    return 
    
	    visited.add(node) 

	    # process current node here. 
	    ...
	    for next_node in node.children(): 
		if next_node not in visited: 
		    dfs(next_node, visited)
