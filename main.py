# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
import random






easy = [
"https://leetcode.com/problems/two-sum/",
"https://leetcode.com/problems/maximum-subarray/",
"https://leetcode.com/problems/valid-parentheses/",
"https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
"https://leetcode.com/problems/house-robber/",
"https://leetcode.com/problems/reverse-linked-list/",
"https://leetcode.com/problems/single-number/",
"https://leetcode.com/problems/merge-two-sorted-lists/",
"https://leetcode.com/problems/climbing-stairs/",
"https://leetcode.com/problems/symmetric-tree/",
"https://leetcode.com/problems/intersection-of-two-linked-lists/",
"https://leetcode.com/problems/reverse-integer/",
"https://leetcode.com/problems/move-zeroes/",
"https://leetcode.com/problems/path-sum-iii/",
"https://leetcode.com/problems/min-stack/",
"https://leetcode.com/problems/invert-binary-tree/",
"https://leetcode.com/problems/merge-two-binary-trees/",
"https://leetcode.com/problems/majority-element/",
"https://leetcode.com/problems/palindrome-linked-list/",
"https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/",
"https://leetcode.com/problems/linked-list-cycle/",
"https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
"https://leetcode.com/problems/diameter-of-binary-tree/",
"https://leetcode.com/problems/shortest-unsorted-continuous-subarray/",
"https://leetcode.com/problems/rotate-array/",
"https://leetcode.com/problems/longest-common-prefix/",
"https://leetcode.com/problems/palindrome-number/",
"https://leetcode.com/problems/maximum-depth-of-binary-tree/",
"https://leetcode.com/problems/jewels-and-stones/",
"https://leetcode.com/problems/search-insert-position/",
"https://leetcode.com/problems/balanced-binary-tree/",
"https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/",
"https://leetcode.com/problems/subtree-of-another-tree/",
"https://leetcode.com/problems/roman-to-integer/",
"https://leetcode.com/problems/convert-bst-to-greater-tree/",
"https://leetcode.com/problems/same-tree/",
"https://leetcode.com/problems/merge-sorted-array/",
"https://leetcode.com/problems/hamming-distance/",
"https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/",
"https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/",
"https://leetcode.com/problems/count-primes/",
"https://leetcode.com/problems/min-cost-climbing-stairs/",
"https://leetcode.com/problems/trim-a-binary-search-tree/",
"https://leetcode.com/problems/non-decreasing-array/",
"https://leetcode.com/problems/island-perimeter/",
"https://leetcode.com/problems/first-unique-character-in-a-string/",
"https://leetcode.com/problems/add-binary/",
"https://leetcode.com/problems/path-sum/",
"https://leetcode.com/problems/longest-univalue-path/",
"https://leetcode.com/problems/happy-number/",
]



medium = [
"https://leetcode.com/problems/longest-substring-without-repeating-characters/",
"https://leetcode.com/problems/add-two-numbers/",
"https://leetcode.com/problems/3sum/",
"https://leetcode.com/problems/longest-palindromic-substring/",
"https://leetcode.com/problems/container-with-most-water/",
"https://leetcode.com/problems/generate-parentheses/",
"https://leetcode.com/problems/number-of-islands/",
"https://leetcode.com/problems/search-in-rotated-sorted-array/",
"https://leetcode.com/problems/longest-increasing-subsequence/",
"https://leetcode.com/problems/find-the-duplicate-number/",
"https://leetcode.com/problems/product-of-array-except-self/",
"https://leetcode.com/problems/word-break/",
"https://leetcode.com/problems/merge-intervals/",
"https://leetcode.com/problems/letter-combinations-of-a-phone-number/",
"https://leetcode.com/problems/subarray-sum-equals-k/",
"https://leetcode.com/problems/maximum-product-subarray/",
"https://leetcode.com/problems/permutations/",
"https://leetcode.com/problems/combination-sum/",
"https://leetcode.com/problems/validate-binary-search-tree/",
"https://leetcode.com/problems/jump-game/",
"https://leetcode.com/problems/kth-largest-element-in-an-array/",
"https://leetcode.com/problems/subsets/",
"https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
"https://leetcode.com/problems/coin-change/",
"https://leetcode.com/problems/course-schedule/",
"https://leetcode.com/problems/word-search/",
"https://leetcode.com/problems/next-permutation/",
"https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
"https://leetcode.com/problems/unique-binary-search-trees/",
"https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
"https://leetcode.com/problems/group-anagrams/",
"https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/",
"https://leetcode.com/problems/sort-colors/",
"https://leetcode.com/problems/binary-tree-inorder-traversal/",
"https://leetcode.com/problems/copy-list-with-random-pointer/",
"https://leetcode.com/problems/task-scheduler/",
"https://leetcode.com/problems/decode-string/",
"https://leetcode.com/problems/search-a-2d-matrix-ii/",
"https://leetcode.com/problems/unique-paths/",
"https://leetcode.com/problems/rotate-image/",
"https://leetcode.com/problems/word-ladder/",
"https://leetcode.com/problems/top-k-frequent-elements/",
"https://leetcode.com/problems/implement-trie-prefix-tree/",
"https://leetcode.com/problems/binary-tree-level-order-traversal/",
"https://leetcode.com/problems/find-all-anagrams-in-a-string/",
"https://leetcode.com/problems/flatten-binary-tree-to-linked-list/",
"https://leetcode.com/problems/queue-reconstruction-by-height/",
"https://leetcode.com/problems/meeting-rooms-ii/",
"https://leetcode.com/problems/sort-list/",
"https://leetcode.com/problems/house-robber-iii/",
]


bloomberg_arr = [
"https://leetcode.com/problems/insert-delete-getrandom-o1/",
"https://leetcode.com/problems/design-underground-system/",
"https://leetcode.com/problems/decode-string/",
"https://leetcode.com/problems/meeting-rooms-ii/",
"https://leetcode.com/problems/number-of-islands/",
"https://leetcode.com/problems/two-city-scheduling/",
"https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/",
"https://leetcode.com/problems/merge-intervals/",
"https://leetcode.com/problems/longest-substring-without-repeating-characters/",
"https://leetcode.com/problems/design-an-ordered-stream/",
"https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/",
"https://leetcode.com/problems/invalid-transactions/",
"https://leetcode.com/problems/all-paths-from-source-to-target/",
"https://leetcode.com/problems/two-sum/",
"https://leetcode.com/problems/lru-cache/",
"https://leetcode.com/problems/word-search/",
"https://leetcode.com/problems/valid-anagram/",
"https://leetcode.com/problems/validate-binary-search-tree/",
"https://leetcode.com/problems/word-break-ii/",
"https://leetcode.com/problems/design-a-leaderboard/",
]






amazon = [
"https://leetcode.com/problems/substring-with-largest-variance/",
"https://leetcode.com/problems/two-sum/",
"https://leetcode.com/problems/sum-of-total-strength-of-wizards/",
"https://leetcode.com/problems/number-of-islands/",
"https://leetcode.com/problems/lru-cache/",
"https://leetcode.com/problems/analyze-user-website-visit-pattern/",
"https://leetcode.com/problems/trapping-rain-water/",
"https://leetcode.com/problems/longest-substring-without-repeating-characters/",
"https://leetcode.com/problems/k-closest-points-to-origin/",
"https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
"https://leetcode.com/problems/group-anagrams/",
"https://leetcode.com/problems/merge-k-sorted-lists/",
"https://leetcode.com/problems/course-schedule/",
"https://leetcode.com/problems/reorder-data-in-log-files/",
"https://leetcode.com/problems/maximum-subarray/",
"https://leetcode.com/problems/valid-parentheses/",
"https://leetcode.com/problems/roman-to-integer/",
"https://leetcode.com/problems/word-ladder/",
"https://leetcode.com/problems/meeting-rooms-ii/",
"https://leetcode.com/problems/sliding-window-maximum/",
]

    


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")

#if user types !easy, bot will send a random easy question
@bot.command()
async def leetcode(ctx):
    easy_question = random.choice(easy)
    medium_question = random.choice(medium)
    #get the problem number and title
    easy_problem_num = easy_question.split("/")[-2]
    easy_problem_title = easy_question.split("/")[-1]
    medium_problem_num = medium_question.split("/")[-2]
    medium_problem_title = medium_question.split("/")[-1]
    msg = f'''
        ***Easy Question*** : {easy_problem_num} {easy_problem_title} \n
        Problem Link: {easy_question} \n
        ***Medium Question*** : {medium_problem_num} {medium_problem_title} \n
        Problem Link: {medium_question} \n



    '''
    await ctx.send(msg)


@bot.command()
async def bloomberg(ctx):
    await ctx.send(f"Bloomberg {random.choice(bloomberg_arr)}" + "\n");

@bot.command()
async def amazon(ctx):
    await ctx.send(random.choice(amazon) + "\n");





bot.run(os.environ["DISCORD_TOKEN"])
