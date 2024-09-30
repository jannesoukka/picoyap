INSERT INTO users (username, is_admin, password_hash) VALUES (
    'user_.',
    't',
    'ie0923'
);
INSERT INTO users (username, is_admin, password_hash) VALUES (
    'testuser',
    'f',
    'ie0923sdadas'
);
INSERT INTO users (username, is_admin, password_hash) VALUES (
    'user2',
    't',
    'ie0923ddddddddd'
);
INSERT INTO users (username, is_admin, password_hash) VALUES (
    'John',
    'f',
    'ie0ssadasda923'
);
INSERT INTO users (username, is_admin, password_hash) VALUES (
    'Clemens',
    'f',
    'ie092sssssssssss3'
);

INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'cats',
    'f',
    'f'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '3',
    'dogs',
    'f',
    'f'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'deletethisplace',
    'f',
    't'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '3',
    'verysecretclub',
    't',
    'f'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'empty',
    'f',
    'f'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '3',
    'veryverysecretclub',
    't',
    'f'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'deletethisplacetoo',
    't',
    't'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'alsoempty',
    'f',
    'f'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'abandonedplace',
    'f',
    't'
);

INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '1',
    '1',
    'So how about them cats, aint they great?',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '2',
    '3',
    'So how about them dogs, aint they great?',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '2',
    '3',
    'So how about them cats, aint they great?',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '4',
    '3',
    'If you see this, you are very cool!',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '1',
    '4',
    'i actually like cats but i wanted a separate one because i HATE the admins!!!!!!!!',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '1',
    '2',
    'I love cars!!!',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '2',
    '5',
    'I like golden retrievers.',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '4',
    '2',
    'i am so cool 😎',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '5',
    '2',
    'FIRST!!!',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '6',
    '1',
    'This place is very very secret',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '4',
    '1',
    'The continuation of our, the admin''s, very very secret conversation.',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '6',
    '1',
    'This place is very very secret part 2',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '4',
    '2',
    'what was that',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '9',
    '3',
    'in here before this place gets abandoned',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '9',
    '4',
    'I will be evil and do illegal stuff',
    'f'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '9',
    '3',
    'PSA: do NOT illegal!!!!',
    'f'
);

INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'I love cats! What do you think?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '3',
    'I love dogs! What do you think?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'Yeah bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'NO I HATE THEM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'STOP YELLING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'no u',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'STOP SPAMMING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'ok i obey you as you are superior in every way',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'i wont muahahahahahahahahaha',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'oh yeah?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I AM SPAMMING AND THERES NOTHING U CAN DO ABOUT IT HAHAHAHAHAHAH',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'hm. awfully quiet around here...',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '4',
    'I HATE YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'L 😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'wow bro u totally showed him',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'yeah bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '2',
    'do you want to be my friend?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '1',
    '1',
    'im busy that day',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '2',
    'yeah bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '3',
    'Cool! Why do you think so?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '2',
    'idk',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '2',
    'their kinda cute i guess',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '5',
    'they''re*',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '2',
    '2',
    'whatever bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '4',
    '3',
    'If you see this message, you are a very cool person. That is because you have been selected to be part of a very secret club!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '4',
    '2',
    'wait i am cool? me? really? 😎?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '4',
    '3',
    'yea bro 😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '4',
    '1',
    'yea bro 😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '4',
    '2',
    'wow bro thats so cool 😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '4',
    'what else am i supposed to add?! look at title!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '2',
    'wow bro thats so mean',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '1',
    'yeah bro knock it off!!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '4',
    'no',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '1',
    'are you sure about that?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '4',
    'oh wait',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '4',
    'you have powers i forgot',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '4',
    'jk i really love admins haha (real, not lying) :)',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '1',
    'yeah thats what i thought',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '2',
    'wow bro you sure showed him',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '1',
    'yeah bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '5',
    '2',
    'can we be friends plz',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '6',
    '2',
    'i love cars!!! they go so fast my mum has one',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '6',
    '3',
    'delete this bro this not on-topic',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '6',
    '2',
    'oh okay i am sorry',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '6',
    '3',
    'its okay you are still very cool',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '6',
    '2',
    'yay!!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '7',
    '5',
    'My uncle had one when i was child, and she was such a nice dog. Why, oh, why must their lifespans be so short?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '2',
    'i am so cool 😎 i am gonna tell my mum',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '3',
    'thats so cool bro 😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '2',
    'yea bro 😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '1',
    '😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '3',
    '😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '2',
    '😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '8',
    '2',
    '😎',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '9',
    '2',
    'FIRST OMG',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '9',
    '3',
    'hey bro delete this its supposed to be empty',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '9',
    '2',
    'oh ok bro im sry',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '9',
    '3',
    'its ok bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '10',
    '1',
    'This place is very very secret and we have not chosen anyone other than admins to have access. We shall discuss very important secret stuff here',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '10',
    '3',
    'I agree. It is very important that we do not leak anything that is discussed here as it is very very secret.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '10',
    '1',
    'I agree with as well. I think we should continue this very very secret discussion on another attoyap I just created. I was totally very careful and checked that I did, in fact, create it on this femtoyap, and not any other femtoyap that is not as very very secret as this place.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '10',
    '3',
    'I agree. Let us migrate.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '11',
    '1',
    'Hello. This the attoyap, in which we shall continue our, the admin''s, very very secret discussion.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '11',
    '2',
    'hey bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '11',
    '3',
    'Hey wrong place!!',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '11',
    '1',
    'Ah crap',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '1',
    'Hello. This is now on the correct femtoyap (the very very secret one), and I was actually very very careful this time.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '3',
    'Fantastic. Let us continue our conversation on very very secret matters.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '13',
    '2',
    'bro i totally just saw an attoyap but its gone now',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '3',
    'Hey, by the way, he totally just our very very secret discussion.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '1',
    'You are correct. This is very concerning. Any ideas?',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '3',
    'Yes. Come to the new attoyap he created. I will say something and you will repeat what I say. Commence operation Gaslight.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '13',
    '3',
    'u saw nothing bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '13',
    '1',
    'u saw nothing bro',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '13',
    '2',
    'ok bro u r right',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '3',
    'I declare operation Gaslight to be a success',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '12',
    '1',
    'That was the most genius move in the history of mankind. I would have never come up with something like that.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '14',
    '3',
    'actually im gonna abandon this place now. i sure hope nothing evil or illegal happens here',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '15',
    '4',
    'i will be evil and illegal here muahahaha',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '15',
    '4',
    'this is an evil message',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '15',
    '4',
    'this is an illegal message',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '15',
    '4',
    'this is a message ultra illegal and evil',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '15',
    '3',
    'this has gone too far!!! do NOT do evil and illegal things here!!! and especially not ULTRA evil and illegal things!!!!! i will delete that ULTRA evil and illegal message because its so ULTRA evil and illegal',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '16',
    '3',
    'do not illegal. it is very very evil and bad so you should not do it. thank you.',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '16',
    '1',
    '👏',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '16',
    '2',
    '👏',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '16',
    '5',
    '👏',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '16',
    '3',
    '🥹',
    'f'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '16',
    '4',
    '😠',
    'f'
);

INSERT INTO secret_permissions (femtoyap_id, user_id) VALUES (
    '4',
    '2'
);