INSERT INTO users (username, is_admin, password_hash) VALUES (
    'user_.',
    't',
    'ie0923'
);
INSERT INTO users (username, password_hash) VALUES (
    'testuser',
    'ie0923sdadas'
);
INSERT INTO users (username, is_admin, password_hash) VALUES (
    'user2',
    't',
    'ie0923ddddddddd'
);
INSERT INTO users (username, password_hash) VALUES (
    'John',
    'ie0ssadasda923'
);
INSERT INTO users (username, password_hash) VALUES (
    'Clemens',
    'ie092sssssssssss3'
);
INSERT INTO users (username, is_admin, password_hash) VALUES (
    'admintest',
    't',
    'scrypt:32768:8:1$LlTvbqb7zPXkXaWF$e14d963ba1bbb6b8bc48b5495efe3446c6f983d77a085895db8aef20fd534f832047faeb7b2c2cdeb268097ec2d503d6d520d0256e3ef8f41ef40a010b64c543'
);

INSERT INTO femtoyaps (creator_id, topic) VALUES (
    '1',
    'cats'
);
INSERT INTO femtoyaps (creator_id, topic) VALUES (
    '3',
    'dogs'
);
INSERT INTO femtoyaps (creator_id, topic, is_deleted) VALUES (
    '1',
    'deletethisplace',
    't'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret) VALUES (
    '3',
    'verysecretclub',
    't'
);
INSERT INTO femtoyaps (creator_id, topic) VALUES (
    '1',
    'empty'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret) VALUES (
    '3',
    'veryverysecretclub',
    't'
);
INSERT INTO femtoyaps (creator_id, topic, is_secret, is_deleted) VALUES (
    '1',
    'deletethisplacetoo',
    't',
    't'
);
INSERT INTO femtoyaps (creator_id, topic) VALUES (
    '1',
    'alsoempty'
);
INSERT INTO femtoyaps (creator_id, topic, is_deleted) VALUES (
    '1',
    'abandonedplace',
    't'
);

INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '1',
    '1',
    'So how about them cats, aint they great?'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '2',
    '3',
    'So how about them dogs, aint they great?'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '2',
    '3',
    'So how about them cats, aint they great?',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '4',
    '3',
    'If you see this, you are very cool!'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '1',
    '4',
    'i actually like cats but i wanted a separate one because i HATE the admins!!!!!!!!'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '1',
    '2',
    'I love cars!!!',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '2',
    '5',
    'I like golden retrievers.'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '4',
    '2',
    'i am so cool 😎'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '5',
    '2',
    'FIRST!!!',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '6',
    '1',
    'This place is very very secret'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title, is_deleted) VALUES (
    '4',
    '1',
    'The continuation of our, the admin''s, very very secret conversation.',
    't'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '6',
    '1',
    'This place is very very secret part 2'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '4',
    '2',
    'what was that'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '9',
    '3',
    'in here before this place gets abandoned'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '9',
    '4',
    'I will be evil and do illegal stuff'
);
INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (
    '9',
    '3',
    'PSA: do NOT illegal!!!!'
);

INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'I love cats! What do you think?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '3',
    'I love dogs! What do you think?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'Yeah bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'NO I HATE THEM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'STOP YELLING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'no u'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'STOP SPAMMING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'ok i obey you as you are superior in every way'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'i wont muahahahahahahahahaha'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'oh yeah?'
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
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'hm. awfully quiet around here...'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '4',
    'I HATE YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'L 😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'wow bro u totally showed him'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'yeah bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '2',
    'do you want to be my friend?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '1',
    '1',
    'im busy that day'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '2',
    'yeah bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '3',
    'Cool! Why do you think so?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '2',
    'idk'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '2',
    'their kinda cute i guess'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '5',
    'they''re*'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '2',
    '2',
    'whatever bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '4',
    '3',
    'If you see this message, you are a very cool person. That is because you have been selected to be part of a very secret club!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '4',
    '2',
    'wait i am cool? me? really? 😎?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '4',
    '3',
    'yea bro 😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '4',
    '1',
    'yea bro 😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '4',
    '2',
    'wow bro thats so cool 😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '4',
    'what else am i supposed to add?! look at title!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '2',
    'wow bro thats so mean'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '1',
    'yeah bro knock it off!!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '4',
    'no'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '1',
    'are you sure about that?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '4',
    'oh wait'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '4',
    'you have powers i forgot'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '4',
    'jk i really love admins haha (real, not lying) :)'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '1',
    'yeah thats what i thought'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '2',
    'wow bro you sure showed him'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '1',
    'yeah bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '5',
    '2',
    'can we be friends plz'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '6',
    '2',
    'i love cars!!! they go so fast my mum has one'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '6',
    '3',
    'delete this bro this not on-topic'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '6',
    '2',
    'oh okay i am sorry'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '6',
    '3',
    'its okay you are still very cool'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '6',
    '2',
    'yay!!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '7',
    '5',
    'My uncle had one when i was child, and she was such a nice dog. Why, oh, why must their lifespans be so short?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '2',
    'i am so cool 😎 i am gonna tell my mum'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '3',
    'thats so cool bro 😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '2',
    'yea bro 😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '1',
    '😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '3',
    '😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '2',
    '😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '8',
    '2',
    '😎'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '9',
    '2',
    'FIRST OMG'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '9',
    '3',
    'hey bro delete this its supposed to be empty'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '9',
    '2',
    'oh ok bro im sry'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '9',
    '3',
    'its ok bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '10',
    '1',
    'This place is very very secret and we have not chosen anyone other than admins to have access. We shall discuss very important secret stuff here'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '10',
    '3',
    'I agree. It is very important that we do not leak anything that is discussed here as it is very very secret.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '10',
    '1',
    'I agree with as well. I think we should continue this very very secret discussion on another attoyap I just created. I was totally very careful and checked that I did, in fact, create it on this femtoyap, and not any other femtoyap that is not as very very secret as this place.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '10',
    '3',
    'I agree. Let us migrate.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '11',
    '1',
    'Hello. This the attoyap, in which we shall continue our, the admin''s, very very secret discussion.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '11',
    '2',
    'hey bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '11',
    '3',
    'Hey wrong place!!'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '11',
    '1',
    'Ah crap'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '1',
    'Hello. This is now on the correct femtoyap (the very very secret one), and I was actually very very careful this time.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '3',
    'Fantastic. Let us continue our conversation on very very secret matters.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '13',
    '2',
    'bro i totally just saw an attoyap but its gone now'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '3',
    'Hey, by the way, he totally just our very very secret discussion.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '1',
    'You are correct. This is very concerning. Any ideas?'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '3',
    'Yes. Come to the new attoyap he created. I will say something and you will repeat what I say. Commence operation Gaslight.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '13',
    '3',
    'u saw nothing bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '13',
    '1',
    'u saw nothing bro'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '13',
    '2',
    'ok bro u r right'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '3',
    'I declare operation Gaslight to be a success'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '12',
    '1',
    'That was the most genius move in the history of mankind. I would have never come up with something like that.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '14',
    '3',
    'actually im gonna abandon this place now. i sure hope nothing evil or illegal happens here'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '15',
    '4',
    'i will be evil and illegal here muahahaha'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '15',
    '4',
    'this is an evil message'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '15',
    '4',
    'this is an illegal message'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content, is_deleted) VALUES (
    '15',
    '4',
    'this is a message ultra illegal and evil',
    't'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '15',
    '3',
    'this has gone too far!!! do NOT do evil and illegal things here!!! and especially not ULTRA evil and illegal things!!!!! i will delete that ULTRA evil and illegal message because its so ULTRA evil and illegal'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '16',
    '3',
    'do not illegal. it is very very evil and bad so you should not do it. thank you.'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '16',
    '1',
    '👏'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '16',
    '2',
    '👏'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '16',
    '5',
    '👏'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '16',
    '3',
    '🥹'
);
INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (
    '16',
    '4',
    '😠'
);

INSERT INTO secret_permissions (femtoyap_id, user_id) VALUES (
    '4',
    '2'
);