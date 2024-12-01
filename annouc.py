from datetime import datetime
from typing import List

class Announcement:
    def __init__(self, title: str, content: str, date: datetime, recipient_groups: List[str]):
        if date < datetime.now():
            print("Error: Announcement date cannot be in the past.")
            return
        self.title = title
        self.content = content
        self.date = date  # Expecting a datetime object
        self.recipient_groups = recipient_groups

    def __str__(self):
        formatted_date = self.date.strftime('%Y-%m-%d %H:%M:%S')  # Format date for better readability
        formatted_content = "\n".join(self.content.splitlines())  # Break content into lines for better display
        return (f"{formatted_date}: {self.title}\n{formatted_content}\n"
                f"(Recipients: {', '.join(self.recipient_groups)})")

    def add_recipient_group(self, group: str) -> None:
        """Adds a new recipient group to the announcement with validation."""
        if not group.isalnum():  # Example: Check if group name is alphanumeric
            print(f"Error: Group name '{group}' is not valid. Please use alphanumeric characters only.")
            return
        if group not in self.recipient_groups:
            self.recipient_groups.append(group)
            print(f"Group '{group}' added to recipients.")
        else:
            print(f"Group '{group}' is already a recipient.")

    def remove_recipient_group(self, group: str) -> None:
        """Removes a recipient group from the announcement."""
        if group in self.recipient_groups:
            self.recipient_groups.remove(group)
            print(f"Group '{group}' removed from recipients.")
        else:
            print(f"Group '{group}' not found in recipients.")

    def add_recipient_groups(self, groups: List[str]) -> None:
        """Adds multiple recipient groups at once."""
        for group in groups:
            self.add_recipient_group(group)

    def is_recipient(self, group: str) -> bool:
        """Checks if a specific group is a recipient."""
        return group in self.recipient_groups
