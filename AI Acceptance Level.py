# Barplot: Compare chatbot attitude scores by AI acceptance level
sns.barplot(data=attitude_by_acceptance, x="AI_Acceptance_Level", y="Avg_Attitude")
plt.title("Average Chatbot Attitude by AI Acceptance Level")
plt.ylabel("Average TUTORT Score")
plt.xlabel("")
plt.tight_layout()
plt.savefig("../outputs/gorseller/attitude_by_acceptance.png", dpi=300)
plt.show()
