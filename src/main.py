from src.reader import read_csv_in_batches, df_to_dict_list
from src.publisher import KafkaPublisher
from src.config import CSV_FILE, BATCH_SIZE



def main():
    publisher = KafkaPublisher()

    for idx, batch in enumerate(read_csv_in_batches(CSV_FILE, BATCH_SIZE), start=1):
        records = df_to_dict_list(batch)
        publisher.publish_batch(records)

if __name__ == "__main__":
    main()
