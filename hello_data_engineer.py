def welcome_message():
    name = "نورالدين"
    role = "Data Engineer"
    goal_days = 30
    
    print(f"اسمي {name}")
    print(f"هدفي: أبقى {role} محترف في {goal_days} يوم")
    print("بدأنا!")

def calculate_progress(current_day, total_days):
    percentage = (current_day / total_days) * 100
    print(f"التقدم: {percentage:.1f}%")

if __name__ == "__main__":
    welcome_message()
    calculate_progress(1, 30)