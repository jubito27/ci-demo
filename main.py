from pathlib import Path

import matplotlib.pyplot as plt  # type: ignore

output_dir = Path(__file__).resolve().parent

print("Step 1-")
fig, ax = plt.subplots()
print("Step 2-")
anime = ['Naruto', 'Luffy', 'Ichigo', 'Eren']
counts = [98, 97, 90, 93]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
print("Step 3-")
ax.bar(anime, counts, label=bar_labels, color=bar_colors)
print("Step 4-")
ax.set_ylabel('Main characters')
print("Step 5-")
ax.set_title('Main characters rating from top 4 anime')
print("Step 6-")
ax.legend(title='Hair c')
print("Step 7-")
plt.savefig(output_dir / 'bars.png', bbox_inches='tight')
print("Step 8-")
cat = ["bored", "happy", "happy", "happy", "happy", "bored"]
dog = ["bored", "bored", "bored", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
print("Step 9-")
fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
print("Step 10-")
ax.plot(activity, cat, label="cat")
print("Step 11-")
ax.legend()
print("Step 12-")
plt.savefig(output_dir / 'lines.png', bbox_inches='tight')
print("Step 13-")