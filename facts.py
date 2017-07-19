# -*- coding: utf-8 -*-

facts = [
    "There are approximately 38,000 known species of spiders. Scientists believe there are probably as many more to be discovered.",
    "Spiders are found on every continent except Antarctica.",
    "An estimated 1 million spiders live in one acre of land. The number might be closer to 3 million in the tropics. It is estimated that a human is never more than 10 feet away from a spider—ever.",
    "The bite of the Brazilian wandering spider can cause long and painful erections, as well as other symptoms, in human males.",
    "Spiders are vital to a healthy ecosystem. They eat harmful insects, pollinate plants, and recycle dead animal and plants back into the earth. They are also a valuable food source for many small mammals, birds, and fish.",
    "Spiders eat more insects than birds and bats combined.",
    "All spiders spin silk, but not all spiders spin webs.",
    "Male spiders weave a small “sperm” web. They then place a drop of semen on the web, suck it up with their pedipalps, and then use the pedipalp to insert the sperm into the female.",
    "Web-weaving spiders have two or three claws at the tip of each leg that they use to swing from strand to strand without getting stuck in the sticky part of their web. Additionally, a spider’s body has a special oily substance that keeps it from getting stuck in its web.",
    "When a spider travels, it always has four legs touching the ground and four legs off the ground at any given moment.",
    "The Bagheera kiplingi is the world’s only (mostly) vegetarian spider.",
    "Abandoned spider webs are called “cobwebs.” The word “cob” is an obsolete word meaning “spider” and is a shortened form of the Old English word attercop, which literally means “poison head.” Etymologists see a connection between cob for spider and cob for corn in that a cob of corn means the “head” or “top” of the corn.",
    "Spider-Man is one of the most popular superheroes. In early comic books, the radioactive spider that bites Peter Parker is incorrectly referred to as an insect.",
    "In rare instances, some spider bites can cause blood disorders. For example, the brown recluse venom may cause red blood cells to burst. This can lead to other symptoms, such as acute kidney injury and jaundice.",
    "Spiders have blue blood. In humans, oxygen is bound to hemoglobin, a molecule that contains iron and gives blood its red color. In spiders, oxygen is bound to hemocyanin, a molecule that contains copper rather than iron.",
    "A spider’s muscles pull its legs inward, but cannot extend its legs out again. Instead, it must pump a watery liquid into its legs to push them out. A dead spider’s legs are curled up because there is no fluid to extend the legs again.",
    "The venom of the black widow spider attacks nerves by blocking their signals to the muscles, which causes the muscles to contract repeatedly and often painfully. Black widow bites can also cause other nerve-related problems, such as high blood pressure, restlessness, and severe facial spasms.",
    "The effects of a spider bite vary according to several factors, including the amount of venom injected and the size and age of the person who was bitten. Children and elderly people are especially susceptible.",
    "Spiders have between two and six spinnerets at the back of their abdomen. Each one is like a tiny showerhead that has hundreds of holes, all producing liquid silk.",
    "Giant trapdoor spiders are considered living fossils because they are similar to spiders that lived over 300 million years ago. They are found in southeastern Asia, China, and Japan and are over 4 inches across, including their legs.",
    "The world’s biggest spider is the goliath spider (Theraphosa blondi). It can grow up to 11 inches wide, and its fangs are up to one inch long. It hunts frogs, lizards, mice, and even small snakes and young birds.",
    "The world’s smallest spider is the Patu marplesi. It is so small that 10 of them could fit on the end of a pencil.",
    "The most deadly spiders in the world include the black widow, funnel web, and brown recluse spiders. One of the most feared spiders in the world, the tarantula, actually has surprisingly weak venom and a bite that feels more like a wasp sting.",
    "The most venomous spider in the world is the Brazilian Wandering Spider, or the banana spider. This aggressive spider wanders the forest floors of Central and South America looking for food. Just a small amount of venom is enough to kill a human.",
    "The brown recluse gets its name from its color and its “shy” nature.",
    "The bite of the brown recluse spider, which is found in the southeastern United States, is particularly dangerous because its bite is initially painless. A person may be bitten without realizing it, but after awhile the skin starts to swell and become incredibly painful. A bite could kill a person if not treated.",
    "Probably the most charming spider in history is Charlotte in E.B. White’s beloved novel Charlotte’s Web. She lives in a barn and saves the life of her good friend, Wilbur the pig.",
    "Arachnophobia is the fear of the spiders. It is one of the most common phobias in North America and Europe. Arachnophobia is less common in tropical places where there are more large, hairy spiders.",
    "The word “spider” comes from the Old English word spithra and is related to the German spinne, both of which mean “spinner.” The word “spinster” is also related and means “one who spins thread.”",
    "While humans have muscles on the outside of their skeleton, spiders have muscles on the inside. A spider’s skeleton, or exoskeleton, covers and protects its muscles.",
    "Some spiders, such as house spiders, are able to run up walls because their feet are covered in tiny hairs that grip the surface. They can’t get out of a bathtub, however, because the surface is too slippery. Other spiders, such as garden spiders, cannot crawl up walls because their legs end in claws, which help them grip threads of silk instead.",
    "Spiders have inspired scientists to make space robots. For example, the “Spidernaut” is a mechanical spider that is designed to crawl over the outside of a spacecraft to carry out repairs. Its weight is spread evenly over its eight legs to avoid damaging the surface of the spacecraft. Scientists have also designed miniature pieces of equipment with parts that move just like a spider’s leg.",
    "The silk that comes out of the spider’s spinneret is liquid, but it hardens as soon as it comes in contact with air. Some spiders have up to seven types of silk glands, each creating a different type of silk—such as smooth, sticky, dry, or stretchy.",
    "The silk in a spider’s web is five times stronger than a strand of steel that is the same thickness. A web made of strands of spider silk as thick as a pencil could stop a Boeing 747 jumbo jet in flight. Scientists still cannot replicate the strength and elasticity of a spider’s silk.",
    "In tropical regions, net-throwing spiders make a small silken web that they throw over their prey.",
    "Hummingbirds use small sticks and the silk from spider webs to weave a nest for themselves.",
    "While most spiders build a new web every day, the web of the gold orb can last several years and can even catch birds.",
    "The funnel web spider is an aggressive spider that attacks and bites people. Its poison has been known to kill in just 15 minutes. Fortunately there is an antivenom, and deaths from this spider are now rare.",
    "Wolf spiders can run at speeds of up to 2 feet per second.",
    "Spiders do not have teeth, so they cannot chew their food. Instead, they inject digestive juices into the innards of their meal. Then the spider sucks up it innards.",
    "Most spiders’ fangs are like pincers that move sideways toward each other to bite. Others, such as bird-eating spiders, have long fangs that point straight down.",
    "Some male spiders give dead flies to the females as presents.",
    "Spiders can’t fly, but they sometimes sail through the air on a line of silk, which is known as “ballooning.”",
    "Water spiders are the only spiders that spend their entire lives in water. The spiders construct a “diving bell” that allows them to live and spin webs underwater. They use their legs like a fishing pole to pull in insects, tadpoles, and even small fish.",
    "The bird-dropping spider gets its name because it looks like bird poo. This type of camouflage prevents birds from eating it.",
    "Two kinds of jumping spiders have been found at 23,000 feet. At this height, no plants grow, but plant material blows up from lower elevations, which is enough to feed the tiny creatures.",
    "Jumping spiders can leap up to 40 times their own body length. If humans could jump this far, they would be able to jump over 230 feet.",
    "Jumping spiders don’t have strong muscle legs. They jump by contracting muscles in their abdomen, which forces liquid into their back legs. The back legs then straighten, which catapults the spider forward.",
    "When a wheel spider gets scared, it tucks in its legs and rolls across the sand.",
    "Hundreds of years ago, people put spider webs on their wounds because they believed it would help stop the bleeding. Scientists now know that the silk contains vitamin K, which helps reduce bleeding.",
    "Some spiders eat their webs and then reuse them.",
    "Spiders are the only group of animals to build webs. Over millions of years, webs have evolved into a variety of kinds, such as sheets, tangles, ladders, and the elegant orb web. When most people think of a web, they think of an orb web.",
    "Scientists in the United States Defense Department are trying to copy gold orb weaver silk in order to use it for bulletproof vests.",
    "The Darwin bark spider creates the strongest material made by a living organism. Their giant webs can span rivers, streams, and even lakes and is 10 times stronger than Kevlar.",
    "Most spiders live alone, meeting other spiders only to mate. A few species of spiders are social and live in groups. For example, in Africa, the web of social spiders such as Stegodyphus colonies can cover whole trees. In India, webs may cover trees for several miles.",
    "Only the bite of the female black widow is dangerous; the male is much smaller than the female, and males and juveniles are harmless to humans. Only the female has the telltale red hourglass shape on its underside; the male has yellow and red bands and spots on the abdomen.",
    "Only female black widows build webs and catch prey. Males do not feed as adults; instead, they concentrate all their effort on mating. A female black widow may sometimes eat a male after mating.",
    "A red widow female spider will begin feeding on the male while they are still mating. However, the male practically force feeds himself to the female by placing himself into her mandibles. If she “spits him out,” he will repeatedly place himself there until she eats him.",
    "Mother spiders can lay as many as 3,000 eggs at one time. Baby spiders are called spiderlings. While most mother spiders do not stay with their babies, the wolf spiders carry their babies on their backs.",
    "Some species of jumping spiders can see light spectrums that humans cannot. Some can see both UVA and UVB light.",
    "A female black widow needs to mate only once. After she has mated, she can produce eggs for the rest of her life, which is about 2 years.",
    "Some tarantulas will fling tiny, irritating hairs, known as urticating hairs, to thwart predators—similar to the way a porcupine uses its quills as defense.",
    "During the 16th and 17th centuries, it was believed that a bite from a species of wolf spider (named tarantula, from the Taranto region in Italy) would be deadly if the victim did not dance to a specific type of frenzied music. It inspired a dance called the tarantella.",
    "Spiders are not insects. They are arachnids, along with scorpions, mites, harvestmen, and ticks. All arachnids have eight legs and two main body parts (a cephalothorax and an abdomen). In contrast, insects have six legs and three main body parts (a head, a thorax, and an abdomen).",
    "Most spiders have eight eyes and are very near sighted. Spiders also have tiny hairs on their legs to help them hear and smell.",
    "Different drugs affect the way spiders spin their webs. For example, spiders on LSD spin beautiful webs, while spiders on caffeine spin terrible webs. Scientists believe that examining the shape of a spider’s web can also help detect airborne chemicals and pollutants.",
    "It is a myth that a human will swallow an average of four (or any number) of spiders while sleeping during his or her life. It is highly unlikely a spider will ever end up in a sleeping human’s mouth.",
    "According to Greek myth, a girl named Arachne could spin so well that the goddess Athena became jealous and turned her into a spider.",
    "A spider has no bones. Rather, it has an exoskeleton, which is like a hard suit of armor that protects its body. Because an exoskeleton does not grow, a spider molts. Typically, a spider molts about 10 times throughout its life.",
    "The bolas spider catches moths using a thick silk thread with a large sticky droplet at the end. The droplet has the same smell as a female moth, which tempts other moths to the trap.",
    "The venom of the female black widow is 15 times more powerful than the poison of a rattlesnake.",
    "A tarantula can liquefy the body of a mouse in just 2 days, leaving behind a pile of just skin and bones.",
    "Most spiders live for about a year. However, some tarantulas live more than 20 years.",
    "The female tarantula hawk wasp feeds her babies tarantulas. She attacks, stings, and paralyzes the huge spider. Afterward, she drags the spider into her lair and lays an egg on it—while the spider is still alive.",
    "Some spiders don’t use webs to catch their prey. Instead, they make a sticky gum, which they fire out through their fangs.",
    "Like rock climbers, many spiders are attached to a line of silk in case they fall. They can also run up it if they need to escape.",
    "Most female spiders are bigger than male spiders.",
    "The black widow and the brown recluse are the only two spiders in North America whose bite can be serious. While the CDC lists the hobo spider as a third toxic spider, some researchers argue that the hobo spider’s venom isn’t as dangerous.",
    "Unlike insects, spiders do not have antennas.",
    "A web is sticky because of glue droplets the spider deposits on it. These droplets are three times thinner than the diameter of a single hair. Scientists describe these droplets as being similar to chewing gum: they just keep stretching and stretching.",
    "Spider webs are not passive traps. Instead, because of electrically conducive glue spread across their surface, webs spring towards their prey. Scientists also found that the glue spirals on the web distort Earth’s electric field within a few millimeters of the web.",
    "Most spiders found in homes have adapted to life indoors. They have little chance of surviving outdoors.",
    "British singer Katie Melua went to a doctor after she heard a “shuffling” in her ear. The doctor discovered that a jumping spider was living in her. She believes the spider climbed into earbud earphones she had used on a flight the previous week.",
    "Spiders are blamed for all kinds of bumps, rashes, and growths. However, unlike mosquitoes or ticks, spiders don’t feed on human blood and they have no reason to bite a human unless they feel threatened or surprised. Additionally, spiders do not typically bite sleeping humans."
]
