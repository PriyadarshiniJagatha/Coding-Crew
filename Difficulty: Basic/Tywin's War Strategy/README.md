<h2><a href="https://www.geeksforgeeks.org/problems/tywins-war-strategy0527/1?page=2&category=Sorting&difficulty=Basic&sortBy=submissions">Tywin's War Strategy</a></h2><h3>Difficulty Level : Difficulty: Basic</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Tywin Lannister is facing a war. He has N troops of soldiers. Each troop has a certain number of soldiers denoted by an array A.<br>
Tywin thinks that a troop is lucky if it has a number of soldiers as a multiple of K. He doesn't want to lose any soldiers, so he decides to train some more.<br>
He will win the war if he has at least half of his troops are lucky troops.<br>
Determine the minimum number of soldiers he must train to win the war.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[ ] = {5, 6, 3, 2, 1} and K = 2
<strong>Output :</strong> 1
<strong>Explanation:</strong>
Troop with 1 soldier is increased to 2.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[ ] = {2, 3, 4, 9, 8, 7} and K = 4<strong>
Output :</strong>  1
<strong>Explanation:
</strong>Troop with 3 soldier is increased to 4. 
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>min_soldiers()</strong> that takes an array <strong>(arr)</strong>, sizeOfArray <strong>(n), </strong>an integer<strong> K,</strong>&nbsp;and return the minimum number of soldiers he must train to win the war. The driver code takes care of the printing.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*LOG(N)).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints :</strong><br>
1 ≤ N, K ≤ 10<sup>5</sup><br>
1 ≤ Ai ≤ 10<sup>5</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Sorting</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;