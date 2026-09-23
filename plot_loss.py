import re
import matplotlib.pyplot as plt

log_file_path = "wandb/offline-run-20260923_130511-ozv49t3c//files//output.log"

steps = []
val_bpb = []
train_bpb = []

pattern = re.compile(
    r"Step\s+(\d+)\s*\|\s*Validation bpb:\s*([\d.]+)\s*\|\s*Train bpb:\s*([\d.]+)"
)

with open(log_file_path, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            steps.append(int(match.group(1)))
            val_bpb.append(float(match.group(2)))
            train_bpb.append(float(match.group(3)))

plt.figure(figsize=(8, 5))
plt.plot(steps, train_bpb, label="Train BPB")
plt.plot(steps, val_bpb, label="Val BPB")
plt.xlabel("Step")
plt.ylabel("Bits Per Byte (BPB)")
plt.title("Train vs Validation BPB")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("bpb_loss_plot.png")
