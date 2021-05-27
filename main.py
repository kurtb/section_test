from transformers import pipeline

def main():
    print(pipeline('sentiment-analysis')('I hate to code!'))

if __name__ == '__main__':
    main()