--[[
    This function will take in a table of intagers and a list of intagers.
    For every intager list it will find the average and then compare it
    with the maximum spam threshold. If the average is greater than it will
    add the key to an array, the function will then return the array.
--]]
function detectSpamm(msgs, max)
    local spam = {}

    for k, v in pairs(msgs) do
        local avg = 0
        for i = 1, #v do
            avg = avg + v[i]
        end
        avg = avg / #v
        if avg > max then
            table.insert(spam, k)
        end
    end

    return spam
end
