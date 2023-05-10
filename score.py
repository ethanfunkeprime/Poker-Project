def score(player_hand: list) -> tuple:
    """
    Determines what type of hand the player holds and assigns it a point value to be used to compare hands to find a winner.
    Card values are: A=14 points, K=13, Q=12, J=11, 10=10, 9=9, 8=8, 7=7, 6=6, 5=5, 4=4, 3=3, and 2=2.
    :param player_hand: List of cards in the player's hand.
    :return: Tuple of the name of the type of hand and a point value to be used to compare hands to find a winner.
    """

    hand_nums = []
    hand_suits = []
    hand_vals = []
    points = 0
    hand_name = ''
    sorted_hand = []

    for card in player_hand:
        hand_nums.append(card[0])
        hand_suits.append(card[1])
        hand_vals.append(card[3])

    for i in range(len(hand_vals)):
        sorted_hand.append(min(hand_vals))
        hand_vals.remove(min(hand_vals))

    if hand_suits[0] == hand_suits[1] == hand_suits[2] == hand_suits[3] == hand_suits[4]:
        if sorted_hand[0] == 10 and sorted_hand[1] == 11 and sorted_hand[2] == 12 and sorted_hand[3] == 13 and sorted_hand[4] == 14:
            hand_name = 'Royal Flush'
            points = 450

        elif sorted_hand[0] == 9 and sorted_hand[1] == 10 and sorted_hand[2] == 11 and sorted_hand[3] == 12 and sorted_hand[4] == 13:
            hand_name = 'Straight Flush'
            points = 449
        elif sorted_hand[0] == 8 and sorted_hand[1] == 9 and sorted_hand[2] == 10 and sorted_hand[3] == 11 and sorted_hand[4] == 12:
            hand_name = 'Straight Flush'
            points = 448
        elif sorted_hand[0] == 7 and sorted_hand[1] == 8 and sorted_hand[2] == 9 and sorted_hand[3] == 10 and sorted_hand[4] == 11:
            hand_name = 'Straight Flush'
            points = 447
        elif sorted_hand[0] == 6 and sorted_hand[1] == 7 and sorted_hand[2] == 8 and sorted_hand[3] == 9 and sorted_hand[4] == 10:
            hand_name = 'Straight Flush'
            points = 446
        elif sorted_hand[0] == 5 and sorted_hand[1] == 6 and sorted_hand[2] == 7 and sorted_hand[3] == 8 and sorted_hand[4] == 9:
            hand_name = 'Straight Flush'
            points = 445
        elif sorted_hand[0] == 4 and sorted_hand[1] == 5 and sorted_hand[2] == 6 and sorted_hand[3] == 7 and sorted_hand[4] == 8:
            hand_name = 'Straight Flush'
            points = 444
        elif sorted_hand[0] == 3 and sorted_hand[1] == 4 and sorted_hand[2] == 5 and sorted_hand[3] == 6 and sorted_hand[4] == 7:
            hand_name = 'Straight Flush'
            points = 443
        elif sorted_hand[0] == 2 and sorted_hand[1] == 3 and sorted_hand[2] == 4 and sorted_hand[3] == 5 and sorted_hand[4] == 6:
            hand_name = 'Straight Flush'
            points = 442

        else:
            if sorted_hand[4] == 14:
                hand_name = 'Flush'
                points = 415
            elif sorted_hand[4] == 13:
                hand_name = 'Flush'
                points = 414
            elif sorted_hand[4] == 12:
                hand_name = 'Flush'
                points = 413
            elif sorted_hand[4] == 11:
                hand_name = 'Flush'
                points = 412
            elif sorted_hand[4] == 10:
                hand_name = 'Flush'
                points = 411
            elif sorted_hand[4] == 9:
                hand_name = 'Flush'
                points = 410
            elif sorted_hand[4] == 8:
                hand_name = 'Flush'
                points = 409
            elif sorted_hand[4] == 7:
                hand_name = 'Flush'
                points = 408
            elif sorted_hand[4] == 6:
                hand_name = 'Flush'
                points = 407
            elif sorted_hand[4] == 5:
                hand_name = 'Flush'
                points = 406
            elif sorted_hand[4] == 4:
                hand_name = 'Flush'
                points = 405
            elif sorted_hand[4] == 3:
                hand_name = 'Flush'
                points = 404
            elif sorted_hand[4] == 2:
                hand_name = 'Flush'
                points = 403

    elif sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3]:
        if sorted_hand[0] == 14:
            hand_name = 'Four of a Kind'
            points = 441
        elif sorted_hand[0] == 13:
            hand_name = 'Four of a Kind'
            points = 440
        elif sorted_hand[0] == 12:
            hand_name = 'Four of a Kind'
            points = 439
        elif sorted_hand[0] == 11:
            hand_name = 'Four of a Kind'
            points = 438
        elif sorted_hand[0] == 10:
            hand_name = 'Four of a Kind'
            points = 437
        elif sorted_hand[0] == 9:
            hand_name = 'Four of a Kind'
            points = 436
        elif sorted_hand[0] == 8:
            hand_name = 'Four of a Kind'
            points = 435
        elif sorted_hand[0] == 7:
            hand_name = 'Four of a Kind'
            points = 434
        elif sorted_hand[0] == 6:
            hand_name = 'Four of a Kind'
            points = 433
        elif sorted_hand[0] == 5:
            hand_name = 'Four of a Kind'
            points = 432
        elif sorted_hand[0] == 4:
            hand_name = 'Four of a Kind'
            points = 431
        elif sorted_hand[0] == 3:
            hand_name = 'Four of a Kind'
            points = 430
        elif sorted_hand[0] == 2:
            hand_name = 'Four of a Kind'
            points = 429
    elif sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
        if sorted_hand[0] == 14:
            hand_name = 'Four of a Kind'
            points = 441
        elif sorted_hand[0] == 13:
            hand_name = 'Four of a Kind'
            points = 440
        elif sorted_hand[0] == 12:
            hand_name = 'Four of a Kind'
            points = 439
        elif sorted_hand[0] == 11:
            hand_name = 'Four of a Kind'
            points = 438
        elif sorted_hand[0] == 10:
            hand_name = 'Four of a Kind'
            points = 437
        elif sorted_hand[0] == 9:
            hand_name = 'Four of a Kind'
            points = 436
        elif sorted_hand[0] == 8:
            hand_name = 'Four of a Kind'
            points = 435
        elif sorted_hand[0] == 7:
            hand_name = 'Four of a Kind'
            points = 434
        elif sorted_hand[0] == 6:
            hand_name = 'Four of a Kind'
            points = 433
        elif sorted_hand[0] == 5:
            hand_name = 'Four of a Kind'
            points = 432
        elif sorted_hand[0] == 4:
            hand_name = 'Four of a Kind'
            points = 431
        elif sorted_hand[0] == 3:
            hand_name = 'Four of a Kind'
            points = 430
        elif sorted_hand[0] == 2:
            hand_name = 'Four of a Kind'
            points = 429

    elif sorted_hand[0] == sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4] and sorted_hand[2] != sorted_hand[3]:
        if sorted_hand[0] == 14:
            hand_name = 'Full House'
            points = 428
        elif sorted_hand[0] == 13:
            hand_name = 'Full House'
            points = 427
        elif sorted_hand[0] == 12:
            hand_name = 'Full House'
            points = 426
        elif sorted_hand[0] == 11:
            hand_name = 'Full House'
            points = 425
        elif sorted_hand[0] == 10:
            hand_name = 'Full House'
            points = 424
        elif sorted_hand[0] == 9:
            hand_name = 'Full House'
            points = 423
        elif sorted_hand[0] == 8:
            hand_name = 'Full House'
            points = 422
        elif sorted_hand[0] == 7:
            hand_name = 'Full House'
            points = 421
        elif sorted_hand[0] == 6:
            hand_name = 'Full House'
            points = 420
        elif sorted_hand[0] == 5:
            hand_name = 'Full House'
            points = 419
        elif sorted_hand[0] == 4:
            hand_name = 'Full House'
            points = 418
        elif sorted_hand[0] == 3:
            hand_name = 'Full House'
            points = 417
        elif sorted_hand[0] == 2:
            hand_name = 'Full House'
            points = 416
    elif sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] == sorted_hand[4] and sorted_hand[1] != sorted_hand[2]:
        if sorted_hand[4] == 14:
            hand_name = 'Full House'
            points = 428
        elif sorted_hand[4] == 13:
            hand_name = 'Full House'
            points = 427
        elif sorted_hand[4] == 12:
            hand_name = 'Full House'
            points = 426
        elif sorted_hand[4] == 11:
            hand_name = 'Full House'
            points = 425
        elif sorted_hand[4] == 10:
            hand_name = 'Full House'
            points = 424
        elif sorted_hand[4] == 9:
            hand_name = 'Full House'
            points = 423
        elif sorted_hand[4] == 8:
            hand_name = 'Full House'
            points = 422
        elif sorted_hand[4] == 7:
            hand_name = 'Full House'
            points = 421
        elif sorted_hand[4] == 6:
            hand_name = 'Full House'
            points = 420
        elif sorted_hand[4] == 5:
            hand_name = 'Full House'
            points = 419
        elif sorted_hand[4] == 4:
            hand_name = 'Full House'
            points = 418
        elif sorted_hand[4] == 3:
            hand_name = 'Full House'
            points = 417
        elif sorted_hand[4] == 2:
            hand_name = 'Full House'
            points = 416

    elif sorted_hand[0] == 10 and sorted_hand[1] == 11 and sorted_hand[2] == 12 and sorted_hand[3] == 13 and sorted_hand[4] == 14:
            hand_name = 'Straight'
            points = 402
    elif sorted_hand[0] == 9 and sorted_hand[1] == 10 and sorted_hand[2] == 11 and sorted_hand[3] == 12 and sorted_hand[4] == 13:
            hand_name = 'Straight'
            points = 401
    elif sorted_hand[0] == 8 and sorted_hand[1] == 9 and sorted_hand[2] == 10 and sorted_hand[3] == 11 and sorted_hand[4] == 12:
            hand_name = 'Straight'
            points = 400
    elif sorted_hand[0] == 7 and sorted_hand[1] == 8 and sorted_hand[2] == 9 and sorted_hand[3] == 10 and sorted_hand[4] == 11:
            hand_name = 'Straight'
            points = 399
    elif sorted_hand[0] == 6 and sorted_hand[1] == 7 and sorted_hand[2] == 8 and sorted_hand[3] == 9 and sorted_hand[4] == 10:
            hand_name = 'Straight'
            points = 398
    elif sorted_hand[0] == 5 and sorted_hand[1] == 6 and sorted_hand[2] == 7 and sorted_hand[3] == 8 and sorted_hand[4] == 9:
            hand_name = 'Straight'
            points = 397
    elif sorted_hand[0] == 4 and sorted_hand[1] == 5 and sorted_hand[2] == 6 and sorted_hand[3] == 7 and sorted_hand[4] == 8:
            hand_name = 'Straight'
            points = 396
    elif sorted_hand[0] == 3 and sorted_hand[1] == 4 and sorted_hand[2] == 5 and sorted_hand[3] == 6 and sorted_hand[4] == 7:
            hand_name = 'Straight'
            points = 395
    elif sorted_hand[0] == 2 and sorted_hand[1] == 3 and sorted_hand[2] == 4 and sorted_hand[3] == 5 and sorted_hand[4] == 6:
            hand_name = 'Straight'
            points = 394

    elif sorted_hand[0] == sorted_hand[1] == sorted_hand[2]:
        if sorted_hand[0] == 14:
            hand_name = 'Three of a Kind'
            points = 393
        if sorted_hand[0] == 13:
            hand_name = 'Three of a Kind'
            points = 392
        if sorted_hand[0] == 12:
            hand_name = 'Three of a Kind'
            points = 391
        if sorted_hand[0] == 11:
            hand_name = 'Three of a Kind'
            points = 390
        if sorted_hand[0] == 10:
            hand_name = 'Three of a Kind'
            points = 389
        if sorted_hand[0] == 9:
            hand_name = 'Three of a Kind'
            points = 388
        if sorted_hand[0] == 8:
            hand_name = 'Three of a Kind'
            points = 387
        if sorted_hand[0] == 7:
            hand_name = 'Three of a Kind'
            points = 386
        if sorted_hand[0] == 6:
            hand_name = 'Three of a Kind'
            points = 385
        if sorted_hand[0] == 5:
            hand_name = 'Three of a Kind'
            points = 384
        if sorted_hand[0] == 4:
            hand_name = 'Three of a Kind'
            points = 383
        if sorted_hand[0] == 3:
            hand_name = 'Three of a Kind'
            points = 382
        if sorted_hand[0] == 2:
            hand_name = 'Three of a Kind'
            points = 381
    elif sorted_hand[1] == sorted_hand[2] == sorted_hand[3]:
        if sorted_hand[1] == 14:
            hand_name = 'Three of a Kind'
            points = 393
        if sorted_hand[1] == 13:
            hand_name = 'Three of a Kind'
            points = 392
        if sorted_hand[1] == 12:
            hand_name = 'Three of a Kind'
            points = 391
        if sorted_hand[1] == 11:
            hand_name = 'Three of a Kind'
            points = 390
        if sorted_hand[1] == 10:
            hand_name = 'Three of a Kind'
            points = 389
        if sorted_hand[1] == 9:
            hand_name = 'Three of a Kind'
            points = 388
        if sorted_hand[1] == 8:
            hand_name = 'Three of a Kind'
            points = 387
        if sorted_hand[1] == 7:
            hand_name = 'Three of a Kind'
            points = 386
        if sorted_hand[1] == 6:
            hand_name = 'Three of a Kind'
            points = 385
        if sorted_hand[1] == 5:
            hand_name = 'Three of a Kind'
            points = 384
        if sorted_hand[1] == 4:
            hand_name = 'Three of a Kind'
            points = 383
        if sorted_hand[1] == 3:
            hand_name = 'Three of a Kind'
            points = 382
        if sorted_hand[1] == 2:
            hand_name = 'Three of a Kind'
            points = 381
    elif sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
        if sorted_hand[2] == 14:
            hand_name = 'Three of a Kind'
            points = 393
        if sorted_hand[2] == 13:
            hand_name = 'Three of a Kind'
            points = 392
        if sorted_hand[2] == 12:
            hand_name = 'Three of a Kind'
            points = 391
        if sorted_hand[2] == 11:
            hand_name = 'Three of a Kind'
            points = 390
        if sorted_hand[2] == 10:
            hand_name = 'Three of a Kind'
            points = 389
        if sorted_hand[2] == 9:
            hand_name = 'Three of a Kind'
            points = 388
        if sorted_hand[2] == 8:
            hand_name = 'Three of a Kind'
            points = 387
        if sorted_hand[2] == 7:
            hand_name = 'Three of a Kind'
            points = 386
        if sorted_hand[2] == 6:
            hand_name = 'Three of a Kind'
            points = 385
        if sorted_hand[2] == 5:
            hand_name = 'Three of a Kind'
            points = 384
        if sorted_hand[2] == 4:
            hand_name = 'Three of a Kind'
            points = 383
        if sorted_hand[2] == 3:
            hand_name = 'Three of a Kind'
            points = 382
        if sorted_hand[2] == 2:
            hand_name = 'Three of a Kind'
            points = 381

    elif sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] and sorted_hand[1] != sorted_hand[2]:
        if sorted_hand[0] == 14 or sorted_hand[2] == 14:
            hand_name = 'Two Pair'
            points = 380
        elif sorted_hand[0] == 13 or sorted_hand[2] == 13:
            hand_name = 'Two Pair'
            points = 379
        elif sorted_hand[0] == 12 or sorted_hand[2] == 12:
            hand_name = 'Two Pair'
            points = 378
        elif sorted_hand[0] == 11 or sorted_hand[2] == 11:
            hand_name = 'Two Pair'
            points = 377
        elif sorted_hand[0] == 10 or sorted_hand[2] == 10:
            hand_name = 'Two Pair'
            points = 376
        elif sorted_hand[0] == 9 or sorted_hand[2] == 9:
            hand_name = 'Two Pair'
            points = 375
        elif sorted_hand[0] == 8 or sorted_hand[2] == 8:
            hand_name = 'Two Pair'
            points = 374
        elif sorted_hand[0] == 7 or sorted_hand[2] == 7:
            hand_name = 'Two Pair'
            points = 373
        elif sorted_hand[0] == 6 or sorted_hand[2] == 6:
            hand_name = 'Two Pair'
            points = 372
        elif sorted_hand[0] == 5 or sorted_hand[2] == 5:
            hand_name = 'Two Pair'
            points = 371
        elif sorted_hand[0] == 4 or sorted_hand[2] == 4:
            hand_name = 'Two Pair'
            points = 370
        elif sorted_hand[0] == 3 or sorted_hand[2] == 3:
            hand_name = 'Two Pair'
            points = 369
        elif sorted_hand[0] == 2 or sorted_hand[2] == 2:
            hand_name = 'Two Pair'
            points = 368
    elif sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4] and sorted_hand[1] != sorted_hand[3]:
        if sorted_hand[0] == 14 or sorted_hand[3] == 14:
            hand_name = 'Two Pair'
            points = 380
        elif sorted_hand[0] == 13 or sorted_hand[3] == 13:
            hand_name = 'Two Pair'
            points = 379
        elif sorted_hand[0] == 12 or sorted_hand[3] == 12:
            hand_name = 'Two Pair'
            points = 378
        elif sorted_hand[0] == 11 or sorted_hand[3] == 11:
            hand_name = 'Two Pair'
            points = 377
        elif sorted_hand[0] == 10 or sorted_hand[3] == 10:
            hand_name = 'Two Pair'
            points = 376
        elif sorted_hand[0] == 9 or sorted_hand[3] == 9:
            hand_name = 'Two Pair'
            points = 375
        elif sorted_hand[0] == 8 or sorted_hand[3] == 8:
            hand_name = 'Two Pair'
            points = 374
        elif sorted_hand[0] == 7 or sorted_hand[3] == 7:
            hand_name = 'Two Pair'
            points = 373
        elif sorted_hand[0] == 6 or sorted_hand[3] == 6:
            hand_name = 'Two Pair'
            points = 372
        elif sorted_hand[0] == 5 or sorted_hand[3] == 5:
            hand_name = 'Two Pair'
            points = 371
        elif sorted_hand[0] == 4 or sorted_hand[3] == 4:
            hand_name = 'Two Pair'
            points = 370
        elif sorted_hand[0] == 3 or sorted_hand[3] == 3:
            hand_name = 'Two Pair'
            points = 369
        elif sorted_hand[0] == 2 or sorted_hand[3] == 2:
            hand_name = 'Two Pair'
            points = 368
    elif sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] and sorted_hand[1] != sorted_hand[2]:
        if sorted_hand[0] == 14 or sorted_hand[2] == 14:
            hand_name = 'Two Pair'
            points = 380
        elif sorted_hand[0] == 13 or sorted_hand[2] == 13:
            hand_name = 'Two Pair'
            points = 379
        elif sorted_hand[0] == 12 or sorted_hand[2] == 12:
            hand_name = 'Two Pair'
            points = 378
        elif sorted_hand[0] == 11 or sorted_hand[2] == 11:
            hand_name = 'Two Pair'
            points = 377
        elif sorted_hand[0] == 10 or sorted_hand[2] == 10:
            hand_name = 'Two Pair'
            points = 376
        elif sorted_hand[0] == 9 or sorted_hand[2] == 9:
            hand_name = 'Two Pair'
            points = 375
        elif sorted_hand[0] == 8 or sorted_hand[2] == 8:
            hand_name = 'Two Pair'
            points = 374
        elif sorted_hand[0] == 7 or sorted_hand[2] == 7:
            hand_name = 'Two Pair'
            points = 373
        elif sorted_hand[0] == 6 or sorted_hand[2] == 6:
            hand_name = 'Two Pair'
            points = 372
        elif sorted_hand[0] == 5 or sorted_hand[2] == 5:
            hand_name = 'Two Pair'
            points = 371
        elif sorted_hand[0] == 4 or sorted_hand[2] == 4:
            hand_name = 'Two Pair'
            points = 370
        elif sorted_hand[0] == 3 or sorted_hand[2] == 3:
            hand_name = 'Two Pair'
            points = 369
        elif sorted_hand[0] == 2 or sorted_hand[2] == 2:
            hand_name = 'Two Pair'
            points = 368
    elif sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4] and sorted_hand[2] != sorted_hand[3]:
        if sorted_hand[1] == 14 or sorted_hand[3] == 14:
            hand_name = 'Two Pair'
            points = 380
        elif sorted_hand[1] == 13 or sorted_hand[3] == 13:
            hand_name = 'Two Pair'
            points = 379
        elif sorted_hand[1] == 12 or sorted_hand[3] == 12:
            hand_name = 'Two Pair'
            points = 378
        elif sorted_hand[1] == 11 or sorted_hand[3] == 11:
            hand_name = 'Two Pair'
            points = 377
        elif sorted_hand[1] == 10 or sorted_hand[3] == 10:
            hand_name = 'Two Pair'
            points = 376
        elif sorted_hand[1] == 9 or sorted_hand[3] == 9:
            hand_name = 'Two Pair'
            points = 375
        elif sorted_hand[1] == 8 or sorted_hand[3] == 8:
            hand_name = 'Two Pair'
            points = 374
        elif sorted_hand[1] == 7 or sorted_hand[3] == 7:
            hand_name = 'Two Pair'
            points = 373
        elif sorted_hand[1] == 6 or sorted_hand[3] == 6:
            hand_name = 'Two Pair'
            points = 372
        elif sorted_hand[1] == 5 or sorted_hand[3] == 5:
            hand_name = 'Two Pair'
            points = 371
        elif sorted_hand[1] == 4 or sorted_hand[3] == 4:
            hand_name = 'Two Pair'
            points = 370
        elif sorted_hand[1] == 3 or sorted_hand[3] == 3:
            hand_name = 'Two Pair'
            points = 369
        elif sorted_hand[1] == 2 or sorted_hand[3] == 2:
            hand_name = 'Two Pair'
            points = 368

    elif sorted_hand[0] == sorted_hand[1]:
        if sorted_hand[0] == 14:
            hand_name = 'One Pair'
            points = 367
        elif sorted_hand[0] == 13:
            hand_name = 'One Pair'
            points = 366
        elif sorted_hand[0] == 12:
            hand_name = 'One Pair'
            points = 365
        elif sorted_hand[0] == 11:
            hand_name = 'One Pair'
            points = 364
        elif sorted_hand[0] == 10:
            hand_name = 'One Pair'
            points = 363
        elif sorted_hand[0] == 9:
            hand_name = 'One Pair'
            points = 362
        elif sorted_hand[0] == 8:
            hand_name = 'One Pair'
            points = 361
        elif sorted_hand[0] == 7:
            hand_name = 'One Pair'
            points = 360
        elif sorted_hand[0] == 6:
            hand_name = 'One Pair'
            points = 359
        elif sorted_hand[0] == 5:
            hand_name = 'One Pair'
            points = 358
        elif sorted_hand[0] == 4:
            hand_name = 'One Pair'
            points = 357
        elif sorted_hand[0] == 3:
            hand_name = 'One Pair'
            points = 356
        elif sorted_hand[0] == 2:
            hand_name = 'One Pair'
            points = 355
    elif sorted_hand[1] == sorted_hand[2]:
        if sorted_hand[1] == 14:
            hand_name = 'One Pair'
            points = 367
        elif sorted_hand[1] == 13:
            hand_name = 'One Pair'
            points = 366
        elif sorted_hand[1] == 12:
            hand_name = 'One Pair'
            points = 365
        elif sorted_hand[1] == 11:
            hand_name = 'One Pair'
            points = 364
        elif sorted_hand[1] == 10:
            hand_name = 'One Pair'
            points = 363
        elif sorted_hand[1] == 9:
            hand_name = 'One Pair'
            points = 362
        elif sorted_hand[1] == 8:
            hand_name = 'One Pair'
            points = 361
        elif sorted_hand[1] == 7:
            hand_name = 'One Pair'
            points = 360
        elif sorted_hand[1] == 6:
            hand_name = 'One Pair'
            points = 359
        elif sorted_hand[1] == 5:
            hand_name = 'One Pair'
            points = 358
        elif sorted_hand[1] == 4:
            hand_name = 'One Pair'
            points = 357
        elif sorted_hand[1] == 3:
            hand_name = 'One Pair'
            points = 356
        elif sorted_hand[1] == 2:
            hand_name = 'One Pair'
            points = 355
    elif sorted_hand[2] == sorted_hand[3]:
        if sorted_hand[2] == 14:
            hand_name = 'One Pair'
            points = 367
        elif sorted_hand[2] == 13:
            hand_name = 'One Pair'
            points = 366
        elif sorted_hand[2] == 12:
            hand_name = 'One Pair'
            points = 365
        elif sorted_hand[2] == 11:
            hand_name = 'One Pair'
            points = 364
        elif sorted_hand[2] == 10:
            hand_name = 'One Pair'
            points = 363
        elif sorted_hand[2] == 9:
            hand_name = 'One Pair'
            points = 362
        elif sorted_hand[2] == 8:
            hand_name = 'One Pair'
            points = 361
        elif sorted_hand[2] == 7:
            hand_name = 'One Pair'
            points = 360
        elif sorted_hand[2] == 6:
            hand_name = 'One Pair'
            points = 359
        elif sorted_hand[2] == 5:
            hand_name = 'One Pair'
            points = 358
        elif sorted_hand[2] == 4:
            hand_name = 'One Pair'
            points = 357
        elif sorted_hand[2] == 3:
            hand_name = 'One Pair'
            points = 356
        elif sorted_hand[2] == 2:
            hand_name = 'One Pair'
            points = 355
    elif sorted_hand[3] == sorted_hand[4]:
        if sorted_hand[3] == 14:
            hand_name = 'One Pair'
            points = 367
        elif sorted_hand[3] == 13:
            hand_name = 'One Pair'
            points = 366
        elif sorted_hand[3] == 12:
            hand_name = 'One Pair'
            points = 365
        elif sorted_hand[3] == 11:
            hand_name = 'One Pair'
            points = 364
        elif sorted_hand[3] == 10:
            hand_name = 'One Pair'
            points = 363
        elif sorted_hand[3] == 9:
            hand_name = 'One Pair'
            points = 362
        elif sorted_hand[3] == 8:
            hand_name = 'One Pair'
            points = 361
        elif sorted_hand[3] == 7:
            hand_name = 'One Pair'
            points = 360
        elif sorted_hand[3] == 6:
            hand_name = 'One Pair'
            points = 359
        elif sorted_hand[3] == 5:
            hand_name = 'One Pair'
            points = 358
        elif sorted_hand[3] == 4:
            hand_name = 'One Pair'
            points = 357
        elif sorted_hand[3] == 3:
            hand_name = 'One Pair'
            points = 356
        elif sorted_hand[3] == 2:
            hand_name = 'One Pair'
            points = 355

    elif sorted_hand[4] == 14:
        hand_name = 'High Card Ace'
        points = 354
    elif sorted_hand[4] == 13:
        hand_name = 'High Card King'
        points = 353
    elif sorted_hand[4] == 12:
        hand_name = 'High Card Queen'
        points = 352
    elif sorted_hand[4] == 11:
        hand_name = 'High Card Jack'
        points = 351
    elif sorted_hand[4] == 10:
        hand_name = 'High Card 10'
        points = 350
    elif sorted_hand[4] == 9:
        hand_name = 'High Card 9'
        points = 349
    elif sorted_hand[4] == 8:
        hand_name = 'High Card 8'
        points = 348
    elif sorted_hand[4] == 7:
        hand_name = 'High Card 7'
        points = 347
    elif sorted_hand[4] == 6:
        hand_name = 'High Card 6'
        points = 346
    elif sorted_hand[4] == 5:
        hand_name = 'High Card 5'
        points = 345
    elif sorted_hand[4] == 4:
        hand_name = 'High Card 4'
        points = 344
    elif sorted_hand[4] == 3:
        hand_name = 'High Card 3'
        points = 343
    elif sorted_hand[4] == 2:
        hand_name = 'High Card 2'
        points = 342

    return hand_name, points
