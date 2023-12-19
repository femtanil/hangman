<template>
    <div class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9"><slot name="formTitle"></slot></h3>
        <form  method="post">
            <div class="grid grid-flow-row">
                <label for="username" class="text-3xl xs:text-4xl">Player name</label>
                <input type="text" id="username" name="username" class="text-3xl xs:text-4xl" />
                <label for="password" class="text-3xl xs:text-4xl">Password</label>
                <input type="password" id="password" name="password" class="text-3xl xs:text-4xl" />
                <input type="submit" value="Start"
                    class=" btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full" />
                <!-- Very unsafe, but it's just a demo -->
                <SelectScreenButton />
            </div>
        </form>
    </div>
</template>
<script setup>
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';
</script>
