MODEL_NAME=ratishsp/Centrum-multinews
#DATASET_NAME=multi_news
#DATASET_NAME=SetFit/bbc-news
#DATASET_NAME=SetFit/20_newsgroups
test_file=20news_newtxt.csv
OUTPUT_DIR=20news_generated_predictions.txt
TARGET_LENGTH=256
MODE=test
text_column=text
summary_column=text

#if centrum used for summary generation:
#script/run_centrum.py \
#--dataset_name ${DATASET_NAME} \
#--text_column ${text_column} \
#--summary_column ${summary_column} \

python script/run_topic.py \
    --model_name_or_path ${MODEL_NAME} \
    --task_name topic \
    --test_file ${test_file} \
    --do_predict \
    --predict_with_generate \
    --logging_dir logs/multi_news_inference \
    --output_dir ${OUTPUT_DIR} \
    --overwrite_output_dir \
    --max_target_length ${TARGET_LENGTH} \
    --val_max_target_length ${TARGET_LENGTH} \
    --max_source_length 4096 \
    --num_beams 5 \
    --prediction_mode ${MODE} \
    --text_column ${text_column} \
    --summary_column ${summary_column} \
    --per_device_eval_batch_size 2