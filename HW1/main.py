from styles import generate_style
from generator import AvatarGenerator

if __name__ == "__main__":
    print(generate_style())
    ag = AvatarGenerator()
    for i in range(5):
        ag.generate(i)
        ag.generate(f"{i}_mle", mle=True)
