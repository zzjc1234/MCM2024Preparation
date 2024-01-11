# Machine Learning

## general workflow

[sklearn-datacamp cheatsheet](https://images.datacamp.com/image/upload/v1676302389/Marketing/Blog/Scikit-Learn_Cheat_Sheet.pdf)

```mermaid
flowchart TD
    start([Start]):::startEnd --> data_collection[Collect Data]:::dataStage
    data_collection --> preprocessing>Preprocess Data]:::processStage
    preprocessing --> data_split{Split \n Data}:::decisionStage
    data_split -.-> train>Training Sets]:::decisionStage
    data_split -.-> test>Test Sets]:::decisionStage
    train -.-> train_model
    test -.-> evaluate_model
    preprocessing --> model_selection{Select Model}:::modelStage
    model_selection --> train_model((Train Model)):::trainStage
    train_model --> evaluate_model{Evaluate Model}:::evaluateStage
    evaluate_model --> |Needs Improvement| hyperparameter_tuning[[Tune Hyperparameters]]:::tuneStage
    hyperparameter_tuning --> train_model
    evaluate_model --> |Meets Criteria| deploy_model{{Deploy Model}}:::deployStage
    deploy_model --> complete([Complete]):::startEnd

    classDef startEnd fill:#fdd,stroke:#333,stroke-width:4px;
    classDef dataStage fill:#fde,stroke:#333,stroke-width:2px;
    classDef processStage fill:#dfe,stroke:#333,stroke-width:2px;
    classDef decisionStage fill:#def,stroke:#333,stroke-width:2px;
    classDef modelStage fill:#fed,stroke:#333,stroke-width:2px;
    classDef trainStage fill:#eef,stroke:#333,stroke-width:4px;
    classDef evaluateStage fill:#fdf,stroke:#333,stroke-width:2px;
    classDef tuneStage fill:#efe,stroke:#333,stroke-width:2px;
    classDef deployStage fill:#dff,stroke:#333,stroke-width:2px;
```


### choice of Model
[SAS cheatsheet](https://blogs.sas.com/content/subconsciousmusings/2020/12/09/machine-learning-algorithm-use/)
[sklearn cheatsheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
[datacamp cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/email/other/ML+Cheat+Sheet_2.pdf)
[azure cheatsheet](https://learn.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet?view=azureml-api-1)

## docs

[ml glossary](https://ml-cheatsheet.readthedocs.io/en/latest/index.html) (WIP)

